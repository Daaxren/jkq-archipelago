# Generating and hosting a JUMP KING QUEST multiworld

Everything here uses only the official Archipelago tools — no extra software.

## 1. Install Archipelago

Download **Archipelago 0.6.7** (the `Setup.Archipelago.exe` installer on Windows) from
<https://github.com/ArchipelagoMW/Archipelago/releases> and install it.

## 2. Install the JKQ world

Double-click `apworld/jump_king_quest.apworld` — the Archipelago Launcher installs it into
`custom_worlds/`. (Manual alternative: copy the file into the `custom_worlds/` folder of your
Archipelago installation.)

## 3. Write one YAML per player

Copy `apworld/JKQ-player-template.yaml`, rename it (e.g. `Mario.yaml`), set `name:` and pick
your options — every line is documented in the file, every option has a default so you can
delete anything you don't care about. Put every player's YAML (JKQ or any other supported
game) into the `Players/` folder of the Archipelago installation.

> **Plando note:** the optional `plando_items` block in the template only works if the machine
> that GENERATES enables it in its `host.yaml`: `plando_options: items` (Launcher → Open
> host.yaml). Not needed otherwise.

## 4. Generate

Run **ArchipelagoGenerate** (or Launcher → *Generate*). The result is a
`AP_<numbers>.zip` in the `output/` folder of the Archipelago installation. That zip is the
whole multiworld: seed, spoiler (if enabled), and one patch/data file per player.

## 5. Host

**Recommended — archipelago.gg (nothing to keep running):**

1. Go to <https://archipelago.gg/uploads> and upload the `AP_….zip`.
2. Click *Create New Room*. The room page shows `archipelago.gg` + a **port** — that pair is
   what every player enters in the in-game Archipelago menu (plus their slot name).
3. The room page also has a text client to spectate/chat and the spoiler download.
   Ports change when a dormant room wakes up — re-check the room page if a reconnect fails.

**Alternative — self-host on your LAN/PC:**

Run `ArchipelagoServer` with the zip. **Caveat for JKQ players on localhost:** the in-process
game client can starve websocket pongs under load and the default `ping_timeout=20s` may drop
it; launch the server with `host/jkq_multiserver_tolerant.py` instead (same MultiServer, with
`ping_timeout=300`):

```
python jkq_multiserver_tolerant.py output/AP_xxxxx.zip
```

(Requires a source checkout of Archipelago 0.6.7 for the import, or run it with the
Archipelago bundled Python. Rooms hosted on archipelago.gg do not need any of this.)

## 6. Play

Each JKQ player: install the client (see the main README), enter host/port/slot in the
in-game **Archipelago** menu, **start a new save**, play. The goal is passing the last door
of the game; when a player goals, their remaining items can be released per the room's
release policy.
