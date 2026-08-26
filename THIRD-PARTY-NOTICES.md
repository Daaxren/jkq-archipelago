# Third-party notices

This package redistributes the following open-source components:

## Archipelago.MultiClient.Net

`client/Archipelago.MultiClient.Net.dll` — based on
[Archipelago.MultiClient.Net](https://github.com/ArchipelagoMW/Archipelago.MultiClient.Net)
6.7.1, **modified**: the websocket transport is replaced with a blocking-I/O RFC 6455
implementation running on dedicated threads (works around a Mono ThreadPool stall in the
game's runtime that delayed or lost deliveries). Licensed under the MIT License; original
copyright the Archipelago.MultiClient.Net contributors.

## Newtonsoft.Json

`client/Newtonsoft.Json.dll` (11.0.1, the build bundled by Archipelago.MultiClient.Net) —
[Json.NET](https://www.newtonsoft.com/json), MIT License, copyright James Newton-King.

## Not redistributed (install separately)

- **BepInEx** 5.4.23.x (LGPL-2.1) — <https://github.com/BepInEx/BepInEx>. The plugin uses the
  HarmonyX API bundled with BepInEx.
- **Archipelago** 0.6.7 — <https://github.com/ArchipelagoMW/Archipelago>, needed to generate
  and host multiworlds.

No files from JUMP KING QUEST (assemblies, assets, saves, or decompiled sources) are included
in this package.

---

MIT License text (applies to the components marked MIT above):

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
