def on_a_pressed():
    if TRex.is_hitting_tile(CollisionDirection.BOTTOM):
        TRex.vy = -220
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_on_destroyed(sprite2):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed)

exit2 = 0
exit3 = 0
projectile: Sprite = None
TRex: Sprite = None
scene.set_background_color(13)
TRex = sprites.create(assets.image("""
    tRex
    """), SpriteKind.player)
TRex.set_position(20, 70)
TRex.ay = 400
tiles.set_tilemap(tilemap("""
    level1
    """))

def on_update_interval():
    global projectile, exit3, exit2
    projectile = sprites.create_projectile_from_side(assets.image("""
        cactus
        """), randint(-200, -120), 0)
    tiles.place_on_tile(projectile, tiles.get_tile_location(9, 5))
    projectile.set_flag(SpriteFlag.AUTO_DESTROY, True)
    exit3 += 1
    if exit3 > 4:
        exit2 = randint(1, 2)
        if exit2 == 2:
            pause(100)
            projectile = sprites.create_projectile_from_side(assets.image("""
                fly
                """), randint(-120, -100), 0)
            tiles.place_on_tile(projectile, tiles.get_tile_location(9, 3))
game.on_update_interval(1500, on_update_interval)
