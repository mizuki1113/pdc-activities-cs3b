# The Mimic Protocol — Room Building Instructions
### For: Vince, Keissha, Josh, Precious
### Date: May 2026

---

## Overview

We are building the game map together. Each person is assigned specific rooms to build in Unity. Everyone works at the same time on separate scene files so there are no conflicts.

The map tells this story:
> Players spawn in the facility, explore through corridors and rooms, find clues, and eventually reach what looks like an exit — but the door is sealed. They discover there is more to the facility. This cliffhanger leads into the next update.

---

## Room Assignments

| Room | Scene File | Assigned To |
|------|-----------|-------------|
| Entrance Hall | `EntranceHall.unity` | Vince |
| Security Room | `SecurityRoom.unity` | Vince |
| Generator Room | `GeneratorRoom.unity` | Precious |
| Main Corridor | `MainCorridor.unity` | Precious |
| Laboratory | `Laboratory.unity` | Keissha |
| Storage Room | `StorageRoom.unity` | Keissha |
| Basement | `Basement.unity` | Josh |
| Maintenance Tunnel | `MaintenanceTunnel.unity` | Josh |
| Sealed Door Room | `SealedDoor.unity` | All (build together last) |

---

## Rules Everyone Must Follow

These rules make sure all rooms connect properly when we merge them:

``` 
Floor level:      Y = 0  (always, no exceptions)
Ceiling height:   4 units
Door width:       3 units
Door height:      3 units
Wall thickness:   0.5 units
Lighting:         Point Lights only (no Directional Light)
Scale:            1 unit = 1 meter
Materials:        Use Assets/Materials folder only
```

> **Important:** If your room doesn't follow these rules, the doors won't line up when we connect the rooms together.

---

## How to Get Started (Everyone Does This First)

### Step 1 — Pull the latest code
Open your terminal in the project folder and run:
```bash
git pull origin main
```

### Step 2 — Create your branch
```bash
# Vince
git checkout -b feature/rooms-vince

# Keissha
git checkout -b feature/rooms-keissha

# Josh
git checkout -b feature/rooms-josh

# Precious
git checkout -b feature/rooms-precious
```

### Step 3 — Open Unity
Open the project in **Unity 6000.4.4f1**. Do NOT open MainScene or GameScene — we will work in separate scene files.

### Step 4 — Create your scene files
For each room you are assigned:
1. Go to **File → New Scene → Basic (Built-in)**
2. Go to **File → Save As**
3. Save in `Assets/Scenes/Rooms/` folder
4. Name it exactly as shown in the Room Assignments table above

---

## How to Build Each Room

### Basic room structure (everyone does this for each room)

**Step 1 — Create the floor**
- Right-click Hierarchy → **3D Object → Plane**
- Name it `Floor`
- Scale: depends on room size (see individual instructions below)
- Position: `X=0, Y=0, Z=0`
- Add a material from `Assets/Materials`

**Step 2 — Create the walls**
- Right-click Hierarchy → **3D Object → Cube**
- Name it `Wall_North`, `Wall_South`, `Wall_East`, `Wall_West`
- Height: `4 units` (Scale Y = 4)
- Thickness: `0.5 units` (Scale Z or X = 0.5)
- Position walls around the floor

**Step 3 — Create the ceiling**
- Right-click Hierarchy → **3D Object → Plane**
- Name it `Ceiling`
- Position Y = `4`
- Same scale as floor

**Step 4 — Add a door opening**
- Leave a gap in one wall that is exactly `3 units wide, 3 units tall`
- This is where rooms connect
- Add a **Cube** named `Door_Frame` around the gap

**Step 5 — Add lighting**
- Right-click Hierarchy → **Light → Point Light**
- Position it at the center of the room at `Y = 3`
- Intensity: `2`
- Range: `10`
- Color: choose based on the room's mood (see individual instructions)

**Step 6 — Add a Box Collider to each wall**
- Select each wall → Add Component → **Box Collider**
- This prevents players from walking through walls

---

## Individual Room Instructions

---

### VINCE — Entrance Hall

**Purpose:** This is where players spawn when the game starts. It should feel like an abandoned industrial facility entrance. Slightly lit, eerie, sets the horror tone.

**Room size:** `20 x 20` (floor plane scale X=2, Z=2)

**What to build:**
- Large open entrance area
- A reception desk (use Cubes to build it) at the center-front
- 2-3 flickering Point Lights (low intensity, slightly red/orange color)
- Broken glass effect using small flat Cubes on the floor
- A door opening on the NORTH wall leading to Main Corridor
- A door opening on the EAST wall leading to Security Room
- Spawn point marker — create an empty GameObject named `SpawnPoint` at `X=0, Y=1, Z=-5`

**Lighting color:** `RGB (255, 200, 150)` — warm but dim, intensity `1.5`

**Objects to add:**
```
- ReceptionDesk (Cube, scale 3x1x1)
- BrokenChair (Cube, scale 0.5x0.5x0.5)
- SpawnPoint (Empty GameObject, Y=1)
- EntranceSign (Cube, flat, on wall)
```

**Atmosphere tip:** Make it feel like the players just broke into an abandoned building. Dusty, dark but not pitch black.

---

### VINCE — Security Room

**Purpose:** A small control room with camera monitors and key storage. Players might find a key here to unlock something later.

**Room size:** `12 x 12` (floor plane scale X=1.2, Z=1.2)

**What to build:**
- A wall of monitor screens (flat Cubes with a dark material, slightly glowing)
- A control desk (Cube)
- A locked cabinet (Cube) that holds a key item
- 1 Point Light, dim green color
- Door opening on the SOUTH wall connecting back to Entrance Hall

**Lighting color:** `RGB (100, 255, 100)` — dim green like old monitors, intensity `1`

**Objects to add:**
```
- ControlDesk (Cube, scale 4x1x1)
- Monitor_1, Monitor_2, Monitor_3 (Cube, flat, on wall)
- KeyCabinet (Cube, scale 1x2x0.5)
- SecurityChair (Cube)
```

**Atmosphere tip:** This room should feel claustrophobic. Low ceiling is fine here (you can lower to 3 units for this room only). Green tint everywhere from the monitors.

---

### PRECIOUS — Generator Room

**Purpose:** The power room. Players may need to interact with the generator to restore power in certain areas.

**Room size:** `15 x 15` (floor plane scale X=1.5, Z=1.5)

**What to build:**
- A large generator in the center (build from Cubes, scale roughly 3x2x2)
- Pipes along the walls (thin long Cubes)
- Warning signs on the walls (flat Cubes with a red material)
- Flickering lights — some Point Lights very low intensity
- Door opening on the SOUTH wall connecting to Main Corridor

**Lighting color:** `RGB (255, 150, 100)` — industrial orange, intensity `1.2`, flickering

**Objects to add:**
```
- Generator (Cube, scale 3x2x2, center of room)
- Pipe_North, Pipe_East (Cube, thin and long, along walls)
- WarningSign_1, WarningSign_2 (flat Cube on wall)
- FuseBox (Cube, on wall)
```

**Atmosphere tip:** Should feel hot and industrial. The generator is broken or barely running.

---

### PRECIOUS — Main Corridor

**Purpose:** The spine of the map. All rooms connect through here. Long, dark hallway with doors on both sides.

**Room size:** `8 x 40` (floor plane scale X=0.8, Z=4) — long and narrow

**What to build:**
- Long narrow corridor
- Door openings on both sides at regular intervals:
  - WEST side: connects to Entrance Hall and Security Room
  - EAST side: connects to Laboratory and Storage Room
  - NORTH end: connects to Generator Room
  - SOUTH end: connects to Basement and Maintenance Tunnel
- Overhead lights along the ceiling (3-4 Point Lights spread along the length)
- Some lights flickering or broken (very low intensity)
- Debris on the floor (small Cubes)

**Lighting color:** `RGB (200, 200, 255)` — cold blue-white fluorescent, intensity `1.5` --could be modified

**Objects to add:**
```
- Debris_1 through Debris_5 (small Cubes scattered on floor)
- CeilingLight_1 through CeilingLight_4 (Point Lights along ceiling)
- BrokenLight (Point Light, very low intensity, flickering)
```

**Atmosphere tip:** This is the scariest part of the map because the Mimic can appear here. Keep it dark between the lights. Players should feel exposed walking through.

---

### KEISSHA — Laboratory

**Purpose:** An old research lab filled with clues about what happened in the facility. Players find notes and items here.

**Room size:** `18 x 14` (floor plane scale X=1.8, Z=1.4)

**What to build:**
- Lab benches along the walls (long flat Cubes)
- Test tube/equipment props (small Cubes on benches)
- A whiteboard on the wall (flat white Cube)
- Bookshelves (Cube stacks)
- A door opening on the WEST wall connecting to Main Corridor
- Papers/documents scattered on the floor (very flat Cubes)

**Lighting color:** `RGB (220, 220, 255)` — cold clinical white, intensity `2`

**Objects to add:**
```
- LabBench_1, LabBench_2 (Cube, scale 5x1x1, along walls)
- Equipment_1 through Equipment_5 (small Cubes on benches)
- Whiteboard (flat Cube on wall, white material)
- Bookshelf_1, Bookshelf_2 (Cube stacks)
- ScatteredPaper_1 through ScatteredPaper_3 (very flat Cubes on floor)
```

**Atmosphere tip:** This room should feel like scientists were working here and suddenly left. Things mid-experiment, chairs knocked over.

---

### KEISSHA — Storage Room

**Purpose:** A supply storage area. Players can find useful items here. Shelves stacked with boxes.

**Room size:** `14 x 14` (floor plane scale X=1.4, Z=1.4)

**What to build:**
- Tall shelving units (Cube stacks, scale 1x4x0.5)
- Boxes on shelves (small Cubes)
- A door opening on the WEST wall connecting to Main Corridor
- Dim single light source — spooky
- Some shelves knocked over (rotated Cubes)

**Lighting color:** `RGB (255, 220, 150)` — dim warm yellow, intensity `1`

**Objects to add:**
```
- Shelf_1 through Shelf_4 (Cube, scale 1x4x0.5, against walls)
- Box_1 through Box_8 (small Cubes on shelves)
- KnockedOverShelf (Cube, rotated sideways on floor)
- StorageCrate (Cube, scale 2x1x1)
```

**Atmosphere tip:** Cramped, claustrophobic. Shelves close together so players have to navigate through narrow paths. Perfect for the Mimic to hide.

---

### JOSH — Basement

**Purpose:** The darkest, most terrifying room. This is the Mimic's primary zone. Players must pass through here to reach the Maintenance Tunnel.

**Room size:** `20 x 20` (floor plane scale X=2, Z=2)

**What to build:**
- Very low lighting — almost pitch black
- Old furniture and broken equipment (Cubes)
- Rusty pipes on the ceiling (long thin Cubes hanging down)
- Water puddles on the floor (very flat Cubes with a reflective dark material)
- A staircase going DOWN from the Main Corridor (Cubes as steps)
- Door opening on the NORTH wall connecting to Maintenance Tunnel

**Lighting color:** `RGB (100, 50, 50)` — very dim deep red, intensity `0.5`

**Objects to add:**
```
- Staircase (series of Cubes as steps, leading down from Y=4 to Y=0)
- BrokenFurniture_1 through BrokenFurniture_3 (Cubes)
- Pipe_Ceiling_1 through Pipe_Ceiling_4 (thin long Cubes hanging from ceiling)
- WaterPuddle_1 through WaterPuddle_3 (very flat Cubes, Y=0.01)
- OldCrate (Cube)
```

**Atmosphere tip:** This is the scariest room. Almost no light. Players should hear their footsteps echoing (tell Josh about the audio). The Mimic spawns here.

---

### JOSH — Maintenance Tunnel

**Purpose:** A tight crawl/walk space connecting the Basement to the Sealed Door room. Players feel trapped here.

**Room size:** `6 x 30` (floor plane scale X=0.6, Z=3) — very narrow and long

**What to build:**
- Extremely narrow corridor
- Pipes on walls and ceiling
- Occasional dim light every 8-10 units
- Debris and obstacles players must navigate around
- Door opening on the SOUTH end connecting to Basement
- Door opening on the NORTH end connecting to Sealed Door room

**Lighting color:** `RGB (150, 150, 100)` — sickly yellow, intensity `0.8`

**Objects to add:**
```
- WallPipe_1 through WallPipe_6 (thin Cubes along walls)
- TunnelLight_1 through TunnelLight_3 (Point Lights, spread along length)
- Debris_1 through Debris_4 (small Cubes blocking path slightly)
- LeakingPipe (Cube with drip effect if possible)
```

**Atmosphere tip:** Players should feel like the walls are closing in. Make it as narrow as playable (6 units is already tight). Very oppressive atmosphere.

---

### ALL — Sealed Door Room (Build Together Last)

**Purpose:** The false exit. Players think they've escaped but the door doesn't open. A message reveals there is more to the facility.

**Room size:** `16 x 16` (floor plane scale X=1.6, Z=1.6)

**What to build:**
- A large imposing door on the NORTH wall (tall Cubes forming a door frame)
- Emergency lighting — red lights
- A sign above the door saying EXIT
- A trigger zone in front of the door
- When player enters trigger zone, a UI message appears

**Lighting color:** `RGB (255, 50, 50)` — emergency red, intensity `1.5`

**The message that appears:**
```
The door is sealed.

There's something beyond this wall...

...but you can't reach it. Not yet.
```

**Script to add (Precious will handle this):**
```csharp
using UnityEngine;
using TMPro;

public class FalseExit : MonoBehaviour
{
    public GameObject messagePanel;
    public TextMeshProUGUI messageText;
    private bool triggered = false;

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && !triggered)
        {
            triggered = true;
            messagePanel.SetActive(true);
            messageText.text =
                "The door is sealed.\n\n" +
                "There's something beyond this wall...\n\n" +
                "...but you can't reach it. Not yet.";
        }
    }
}
```

---

## When You Are Done — How to Push Your Work

### Step 1 — Save your scene
Press **Ctrl+S** in Unity.

### Step 2 — Commit and push
Open your terminal and run:
```bash
git add .
git commit -m "feat: built [your room names] - [your name]"
git push origin feature/rooms-[yourname]
```

**Example commit messages:**
```bash
# Vince
git commit -m "feat: built EntranceHall and SecurityRoom - Vince"

# Keissha
git commit -m "feat: built Laboratory and StorageRoom - Keissha"

# Josh
git commit -m "feat: built Basement and MaintenanceTunnel - Josh"

# Precious
git commit -m "feat: built GeneratorRoom and MainCorridor - Precious"
```

### Step 3 — Create a Pull Request
1. Go to the GitHub repository
2. Click **Pull Requests → New Pull Request**
3. Base: `main` ← Compare: `feature/rooms-yourname`
4. Title: `feat: [Your Name] room builds`
5. Click **Create Pull Request**
6. Tag Precious to review

---

## Things NOT to Do

- ❌ Do NOT push directly to `main`
- ❌ Do NOT open or edit `MainScene` or `GameScene`
- ❌ Do NOT add a Directional Light (we already have one in GameScene)
- ❌ Do NOT change the Player prefab
- ❌ Do NOT move or rename anyone else's scene files
- ❌ Do NOT use assets that aren't already in the project

