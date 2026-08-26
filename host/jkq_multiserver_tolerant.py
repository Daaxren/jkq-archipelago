"""Tolerant local MultiServer launcher for JUMP KING QUEST.

Root cause (S7 investigation, 2026-07-26): the stock server uses the `websockets` library
defaults — ping every 20s, close the connection if the pong does not arrive within 20s.
Inside the Unity/Mono game process, engine stalls (loads, GC pauses) can starve the client's
pong replies past that window, so the SERVER closes a perfectly healthy session mid-play
(a 40-minute headless idle probe with the same client stack never dropped once).

This launcher raises the ping tolerance for LOCAL hosting only (pings still flow every 20s,
but a stall now has 300s of grace before the server gives up — TCP and the client's own
in-process reconnect cover genuine deaths). The pinned Archipelago tree is NOT modified.

Usage (from the repo root, same arguments as MultiServer.py):
    .venv-ap\\Scripts\\python.exe scripts\\jkq_multiserver_tolerant.py --port 38296 path\\to\\AP_seed.zip
"""
import os
import sys

_AP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "external", "Archipelago"))
sys.path.insert(0, _AP_DIR)

import websockets  # noqa: E402  (resolved from the AP venv)

_orig_serve = websockets.serve


def _tolerant_serve(*args, **kwargs):
    # v5.5n: ping FREQUENTLY (3s, not 20s). Root cause of the prison send-wedge: after ~100s of idle
    # climbing, Mono's ClientWebSocket ReceiveAsync is blocked waiting for a DATA frame and Mono cannot
    # SendAsync while a receive is pending, so the first check-send after idle hangs indefinitely. A
    # frequent server ping cycles the client's receive machinery every ~3s, so a pending send waits at
    # most a few seconds instead of forever. ping_timeout stays huge (300s) so the frequent pings never
    # cause a false drop even if the heavy client pongs slowly.
    kwargs["ping_interval"] = 3
    kwargs["ping_timeout"] = 300
    return _orig_serve(*args, **kwargs)


websockets.serve = _tolerant_serve

import asyncio  # noqa: E402

import MultiServer  # noqa: E402

if __name__ == "__main__":
    print("[jkq] tolerant launcher: websocket ping_timeout raised to 300s (local hosting)")
    try:
        asyncio.run(MultiServer.main(MultiServer.parse_args()))
    except asyncio.exceptions.CancelledError:
        pass
