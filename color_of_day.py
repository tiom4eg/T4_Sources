def creator():
    from PIL import Image
    from random import randint
    hexer = randint(0, 16777215)
    image = Image.new("RGB", (100, 100), f"#{hex(hexer)[2:]}")
    image.save("discord.png", "PNG")


creator()
