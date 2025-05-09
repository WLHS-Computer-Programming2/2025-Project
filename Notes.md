## Pygame keyboard input: two complementary approaches

| **Call** | **What you get** | **How long it’s valid** |
|----------|------------------|-------------------------|
| `for event in pygame.event.get(): …` → `event.key` | The **next event** just popped from Pygame’s **event queue** (`KEYDOWN`, `KEYUP`, mouse click, `QUIT`, …). | Only during that loop iteration—once processed, the event is gone. |
| `pygame.key.get_pressed()` | A tuple giving the **pressed / not‑pressed state of *every* key** *at the instant you call it*. | Until you call it again (usually once per frame). |

---

### Why `get_pressed()` must live *outside* the event loop

Most frames generate **no new events**, especially when you’re merely *holding* a key.  
If you put

```python
keys = pygame.key.get_pressed()
```
inside

```
for event in pygame.event.get():
```

that line runs zero times on frames with an empty event queue, so your character doesn’t move even though the key is still held.

Move it outside the loop so it executes every frame.

## Typical Structure
```
while True:                     # --- game loop ---
    # 1. Handle discrete, one‑off events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shoot()             # happens once when spacebar is pressed

    # 2. Handle continuous input
    keys = pygame.key.get_pressed()      # snapshot once per frame
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 10                   # runs every frame key is held
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 10
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 10

    draw()                    # render everything
    pygame.display.update()
    clock.tick(60)            # 60 FPS
```

## Quick recap

1. Event queue (event.get, KEYDOWN, KEYUP): use for actions that occur once (fire bullet, open menu, toggle fullscreen).

2. Key‑state poll (key.get_pressed): use for actions that happen every frame a key is held (smooth movement, camera scrolling).

Process all events first, then poll the keyboard once per frame, and your input logic remains simple and reliable.

## Single key press

```
# if event.type == pygame.KEYDOWN: # if key is pressed down and released
        #     if event.key in (pygame.K_UP, pygame.K_w):
        #         player.y -= 10
        #     if event.key in (pygame.K_DOWN, pygame.K_s):
        #         player.y += 10
        #     if event.key in (pygame.K_LEFT, pygame.K_a):
        #         player.x -= 10
        #     if event.key in (pygame.K_RIGHT, pygame.K_d):
        #         player.x += 10
```