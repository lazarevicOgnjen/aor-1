import os
from dhooks import Webhook, Embed, File

image2_path = 'cs elfak.jpg'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[AOR-1 main page link - click here -](https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=139)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs elfak.jpg")
    file = File(image2_path, name="cs elfak.jpg")
    hook.send("@everyone 📢 AOR-1", embed=embed, file=file)
