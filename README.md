# JUMP KING QUEST — Archipelago

An [Archipelago](https://archipelago.gg) multiworld randomizer for **JUMP KING QUEST** on [Steam](https://store.steampowered.com/app/2317640/JUMP_KING_QUEST/).

- **Client**: a BepInEx 5 plugin (`client/`) — connects the game to an Archipelago server,
  turns pickups/shops/quests/bosses into checks, delivers multiworld items in game with native
  popups, and sends the goal when you pass through the last door of the game.
- **World**: an Archipelago APWorld (`apworld/`) — used to generate the multiworld seed.
  870 locations, world version **0.9.0**, Archipelago **0.6.7**.

> **Status: beta.** Single-player-offline game sessions only (the plugin refuses to run
> alongside JKQ's native online). Nothing from the game is redistributed here: no game files,
> no assets — only this project's own code and its open-source dependencies.

## What's randomized

By default:

- **All weapons and shields** not sold by NPCs.
- **All key items** except Humoral Slop, Key to your Cell, Nascent Doubts, Emoaian Pins,
  Gargoyle's Ash, Hog Caller and Terrible Toot Lure.
- The **Starter Class Pack** — a single item which includes all the starting items of your
  character's Inclination. It is a single item because the randomizer has no control over which
  class the player chooses, and the number of starting items varies between Inclinations:
  Deprived only starts with Paper Bag, while Stringent has all the armor set pieces, Bow and
  Arrows.

Everything else — armor sets, shops, the Emoaian economy,
upgrades, consumables and more — joins the pool through the [YAML options](#yaml-options) below.

## Requirements

- JUMP KING QUEST on [Steam](https://store.steampowered.com/app/2317640/JUMP_KING_QUEST/), current build (V.1.1.0:661).
- [BepInEx 5.4.23.x, x64](https://github.com/BepInEx/BepInEx/releases) (5.4.23.5 recommended).
- [The JKQ-Archipelago Release](https://github.com/Daaxren/jkq-archipelago/releases) (the zip).
- To generate/host a seed: [Archipelago 0.6.7](https://github.com/ArchipelagoMW/Archipelago/releases)
  — see [`docs/GENERATE.md`](docs/GENERATE.md).

## Installation

1. Install **BepInEx 5 (x64)** into the JUMP KING QUEST/ game folder: unzip it next to the game exe, run the
   game once, close it. `BepInEx/plugins` folder appears.
   To find your /JUMP KING QUEST game folder: go in your Steam Library → right click on JUMP KING QUEST → Manage → Browse local files.
2. Manually create the folder `BepInEx/plugins/JKQArchipelago.NetworkSlice/` and copy the three DLLs
   from the downloaded zip [`client/`](client/) into it:
   - `JKQArchipelago.NetworkSlice.dll`
   - `Archipelago.MultiClient.Net.dll`
   - `Newtonsoft.Json.dll`

## Joining a Multiworld

1. Launch the game. In the **main menu** there is now an **Archipelago** button:
   enter host (`archipelago.gg`), port, slot name and password, then **Save & Connect**.
2. **First installation only:** the dialog answers *"Saved. RESTART the game to connect…"* — close the
   game and launch it again. This happens once per install (the first Save & Connect is what
   enables the mod, and it arms only at startup). From then on the game connects **by itself**
   at the main menu on every launch, and changing room/port from the dialog is live — no more
   restarts.
3. **Start a NEW save** for a new seed (recommended: one save per seed).
4. Play.

## Generate & host a game

Full step-by-step (no tooling beyond Archipelago itself): [`docs/GENERATE.md`](docs/GENERATE.md).
Short version: install the latest Archipelago build → double-click `apworld/jump_king_quest.apworld` →
put one YAML per player (start from [`apworld/JKQ-player-template.yaml`](apworld/JKQ-player-template.yaml)) in `Players/` →
**Generate** → upload the output zip at <https://archipelago.gg/uploads> → create the room and share host/port.

## YAML options

Options go in your player YAML (start from
[`apworld/JKQ-player-template.yaml`](apworld/JKQ-player-template.yaml), where every option is
also documented inline). Everything below is **off / vanilla by default**.

- **`better_gurglevale`** — after you use the Damp Rusting Key the rest of the game is basically
  open world until the Wrench is needed to finish the game. This option tries to reduce this
  huge sphere into smaller ones without customizing the game too much:
  - Dirty Key now opens the door between Graveyard Basin and Gurgling Gorge;
  - the door that connects Tyrant's Ravine and Gurgling Gorge can now be opened from the
    Gurgling Gorge side only — so either Gurgling Tower Key or Dirty Key is required to reach
    Cockatrice and proceed with the game;
  - Kitchen Key is now needed to open Gnoddrick's arena door (in vanilla you can completely
    ignore Kitchen Key with a pretty easy shield jump under the last Igor spot in Famished
    Fortress).
- **`cell_key`** (`vanilla`/`shuffled`) — randomize the Key to your Cell, needed to open the door
  in the first room of the game. If shuffled, you only have one reachable location before having
  to wait to receive the key in order to progress.
- **`hotdog`** (`vanilla`/`shuffled`) — randomize the Eternial Hotdog used to heal.
  **Warning:** if shuffled, you could be expected to beat the whole game without the Eternial
  Hotdog.
- **`shuffle_armor`** — shuffle the armor sets (Helmets, Torsos, Gloves, Boots, Hats and Bases).
- **`shuffle_brownkloake_shop`** — shuffle weapons, shields and armors sold by Brownkloake.
- **`random_brownkloake_prices`** — randomize the marble prices in Brownkloake's shop: each offer
  is priced at a random number of marbles between **`brownkloake_minimum_price`** and
  **`brownkloake_maximum_price`** (defaults 10–500; if the maximum ends up below the minimum,
  the two are swapped). For scale: vanilla Brownkloake prices sit in the low hundreds, so
  anything past a few thousand turns his shop into a marble grind.
- **`emoaiansanity`** — shuffle Emoaian Pins, the Emotes sold by Emoaian Statue NPCs for Emoaian
  Pins, and the Emotes gifted by NPCs (Ook, Combat Stance, Pray, Relaxing Break, Carefree
  Break).
- **`shuffle_doubts`** — shuffle the Nascent Doubts used to respec your character's attributes.
- **`shuffle_whetstones`** — shuffle the Whetstone items used to upgrade weapons.
- **`shuffle_filaments`** — shuffle the Reinforced Filaments used to upgrade armor.
- **`shuffle_wisdom`** — shuffle the Wisdom pickups used to obtain Insight (all sizes).
- **`shuffle_marbles`** — shuffle the Marble Saccs used to obtain Marbles (all sizes).
- **`shuffle_ammo`** — shuffle ammunition packs (Arrows, Bolts and Acorns).
- **`shuffle_consumables`** — shuffle Chicken Wings, Frog Legs, Cigarettes, Packs of Cigarettes,
  Cigars, Coffee, Holy Water and Mud Oile.
- **`lobotomy_language`** — all in-game text is in Lobotomy Curse's Gibberish. Purely cosmetic,
  it doesn't affect the logic — implemented for fun so you can enjoy the Gibberish without the
  other annoyances of the Lobotomy Curse.
- **`death_link`** — standard Archipelago DeathLink: when you die, every DeathLink player dies;
  when any of them dies, so do you.

## Differences from the base game

- **Handmaidens can be used freely**, without links. This is both QoL and softlock prevention,
  in case you drop down to Bog Shallows before obtaining all the progression items you need.
- **A new Handmaiden has been added right after Warden**, so no items in Redfin Prison are
  missable.
- The Cigarette just after entering Kingswood has been replaced by the **Kingswood Key**: a
  custom key item now required to open Zanzibart's Arena (it reuses the sprite of the removed
  item Redcrown Gate Key). In vanilla, if you progress far enough through the story, Zanzibart's
  arena becomes inaccessible — this change exists to avoid that softlock.
- The **Wave** emote can no longer be bought from the Emoaian NPCs and is only gifted by the
  Emoaian NPC in Redfin Prison.
- Old Man and Igor **won't give you the Eternial Hotdog** if you don't have it.
- Old Man only trades with hairy nuts in **Mangrove Pits**, not Bog Beach, due to limitations.

## Good to know

- **Saves are independent from the room.** You can switch character/save in the same Archipelago room; the client re-binds automatically.
  This is not the intended way to play. Each character keeps its own inventory and flags while the Archipelago world is shared, items already received in another save will be voided.
- **Offline-tolerant.** A pickup collected while the connection is down is recorded durably and
  delivered when the connection returns — never lost, never doubled.
- The Archipelago dialog has a **Disconnect** button: it turns auto-connect off
  so the game stays vanilla from then on (immediate at the main menu; if you already played a
  save this launch, it takes effect at the next restart). Save & Connect turns it back on.
- Logs: `BepInEx/LogOutput.log`, lines prefixed `[JKQAP-NET]` — attach them to any bug report,
  **together with `BepInEx/JKQAP-events.log`** (a crash-proof copy of the same events: if the game
  freezes or is killed, this file keeps the final seconds that `LogOutput.log` can lose).
- **Goal**: pass the **last door** of the game (top of Phantom Tower final stairs).
- **Don't sell progression items!** You can sell items that are needed to obtain checks (like
  the Frog King armor pieces), making some quests impossible to complete — and potentially the
  whole Archipelago unbeatable.
- **Curses are NOT considered in logic** and, especially Bogged, should be avoided. Some cool
  curses that don't alter the logic: Trust in Fortune (use what you receive), Golden Fingers
  (useful for shopsanity) and Brittle Bones (brutal with DeathLink).
- Black Knight skip and Kitchen Key skip are not considered in logic.
- You can escape your starting cell using shield surfing: not considered in logic.
- Logic expects you to have the **Torch** in every dark room in Phantom Tower except the one at the very bottom.
- Logic expects you to pull the lever in Phantom Tower to explore the dark area with the
  floating skulls.
- **All weapons are progression items**, since you need at least one to get over the wooden wall
  in Redfin Prison and to actually defeat bosses. The game may therefore expect you to use a
  ranged weapon even if you don't have ammo for it.
- **Stacks of items are separate locations** — the four Emoaian Pins from the Emoaian NPC in
  Boglink Shrine, or the two Mud Oiles in the same chest in Fungal Fields: two separate Mud
  Oiles join the item pool and two items are found in that chest. The exceptions are ammo packs
  (it would be insane) and the Starter Class Pack chest, which is a single item since you could
  start the game as Deprived, which only receives the Paper Bag.
- **Not randomized for now**: the items tied to Bellman's and Percy's quests (Red Crown Bugle,
  Letter from Percy, Laugh, Facepalm, Percy's Old Rapier, Bellman's Replica Set — most of them
  are missable and cryptic), the Hero of Kraxa armor set, and the Krulk Battalion set (missable
  if you do bosses in a weird order).
- The three **DLC armor sets** are not randomized and never will be, in order to respect
  Nexile's business decisions. You can decide to ignore them if you don't want to ruin your
  randomized run.

## Base game FAQs

- The Gladiator NPC leaves behind his weapon and armor set after you exhaust his dialogue and
  defeat Oinko, then reload Boglink Shrine.
- The Emoaian NPC sells you the Emoaian Headdress after you interact with 6 different Emoaian
  NPCs other than the one in Boglink Shrine.
- Foods cap at 5: if you already have 5 Raw Frog Legs in your inventory and one arrives from the
  multiworld, it gets voided.

## Future ideas

Nothing here is promised — it's the wishlist:

- shuffle the missing items (Bellman's and Percy's quest items, Hero of Kraxa set, Krulk
  Battalion set, Gargoyle's Ash, Hog Caller and Terrible Toot Lure);
- shuffle levers;
- randomize item levels;
- MacGuffin Hunt goal (Triforce Hunt);
- full shopsanity (Dreeg, Dirtclaat and the Gargoyles);
- Brownkloake minimum price 0 instead of 1, to enable Poverty runs with shopsanity;
- randomize roaming bosses drops;
- Brambleon logs shuffle;
- crow spots as locations;
- Curse traps and Hog Caller trap;
- enemizer and boss shuffle;
- BGM shuffle.

## Troubleshooting

| Symptom | Meaning |
|---|---|
| `network_build_check supported=false` in the log | Game build not supported by this plugin build — the plugin stays disarmed (safe). Update the package. |
| No Archipelago button in the menu | BepInEx not loaded (no `BepInEx/LogOutput.log`?) or DLLs in the wrong folder. |
| "Room found — logged in" but nothing in game | Load a save — the connection binds to a save, checks only flow in game. |
| Checks feel delayed when self-hosting locally | Use `host/jkq_multiserver_tolerant.py` to launch the local server (raises `ping_timeout`; see GENERATE.md). Rooms on archipelago.gg are unaffected. |

## Credits & licenses

This project is released under the [MIT License](LICENSE). Bundled third-party components:
see [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md).

- Gameplay guide, options design and base-game research by **Rikkukun** — this randomizer was
  developed alongside him, and there would be no release without his game knowledge and testing.
- Thanks to **Cam** (cammycal) and **Boo** (bookiskookis) from the official Archipelago Discord
  for their valuable insights during development.
- Thanks to **Fajacopo** for drawing the Archipelago icon in the style of JKQ.
- Built entirely using **Claude AI** (Anthropic's Claude Code) as the development tool.

Not affiliated with the developers of JUMP KING QUEST or with Archipelago.
