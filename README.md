# TOTK Stick Summoner

First prototype: **swing a Stick -> spawn one Bokoblin**.

Target: TOTK 1.4.3 on Nintendo Switch.

The project is being built around the user's own extracted TOTK files. Nintendo game assets are not redistributed here.

The important part is a real weapon-swing trigger plus an actor-spawn call. A plain weapon-data edit cannot perform that behavior, so the build must use the appropriate runtime/event hook rather than pretending a data-only mod is finished.

## Prototype behavior

1. Link equips the Stick.
2. Link swings/attacks.
3. The mod detects that weapon swing.
4. Exactly one Bokoblin is spawned in front of Link.

After this works, the same mapping can be expanded to the enemy tiers and special enemies requested for the full Ultra Mods project.
