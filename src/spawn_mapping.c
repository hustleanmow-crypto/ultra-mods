#include <stddef.h>

typedef struct {
    const char *weapon_actor;
    const char *enemy_actor;
    int count;
} SpawnRule;

// First rule for the prototype. The actual weapon-swing hook is supplied by
// the target TOTK runtime layer; this table keeps the gameplay mapping simple.
static const SpawnRule stick_rule = {
    "Weapon_Sword_001",
    "Enemy_Bokoblin_Junior",
    1
};

const SpawnRule *stick_bokoblin_rule(void) {
    return &stick_rule;
}
