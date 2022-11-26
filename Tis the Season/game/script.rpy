define kane = Character(("Kane"), color = "#be392a")
define chris = Character(("Chris"), color = "#22772e")
define felix = Character(("Felix"), color = "#2c4b65")
define jack = Character(("Jack"), color = "#be392a")
define holly = Character(("Holly"), color = "#00FF00")
define noelle = Character(("Noelle"), color = "#22772e")

define hs = Character(("Hotel Receptionist"))

# The game starts here.

label start:

    #scene bg office

    # scene 1
    #start this properly

    "(talking)"

    show kane

    kane "You'd better not be thinking about getting me anything for Christmas, Holly."

    "My boss and fiancé, Kane. He's nice, but a bit of a Scrooge!"

    holly "Hi, babe!"

    kane "Don't forget about the important meeting at our company headquarters in the big city. We're closing an expensive deal."

    holly "I can't believe we're having a big meeting so close to Christmas! And so far away too. Flights are so expensive!"

    kane "I don't make the rules, Holly. If flights are so expensive you can just drive."

    hide kane

    #scene 2
    scene bg road

    "I decided to drive. Who doesn't love a good roadtrip?"
    "It's a long drive though... I'll take a break. There's a town coming up, a little place called Mistletoe."
    "I might as well stop by on the way."

    #show bg town

    "Gosh, it's so gorgeous here... I miss small town life. Living in the city just isn't the same"
    "As I get out of the car, I step on a patch of ice and go flying."
    holly "Whoa!"
    "But before I hit the ground, someone catches me."
    
    show jack
    with fade

    jack "Hey, careful there!"
    "He's so handsome!"
    holly "I-"
    jack "The roads get real icy around here in the winter."
    holly "Sorry-"
    jack "Don't worry about it. I'm jack."
    holly "I'm Holly."
    "We look at each other for a moment."
    holly "How did you know I'm from out of town?"
    jack "It's a small town. I know everyone here."
    "Wow, a real small town man."
    holly "Well, do you know where I can get a coffee? I've been driving for a while."
    jack "There's a café called Jingle Bell Bakery just north of here on the left." 
    "He points north for emphasis."
    jack "I know you wanted coffee, but they have the best hot chocolate in the state."
    holly "Well, thanks for the help."
    "That was SO awkward!"

    hide jack

    #scene bg town 2
    #with fade

    "Ugh, I'm lost! Where's this freakin bakery!"

    show noelle

    noelle "Hi lady!!! Are you lost??"
    "Woah! What a cute child!"
    holly "I am a bit... do you know where Jingle Bell Bakery is?"
    noelle "Uhhh..."
    noelle "No."
    noelle "My daddy can help you though!"
    "Her dad? What's she up to?"
    noelle "come on!"

    show noelle at right
    show chris at left

    noelle "Daddy! Help this nice lady with directions!"
    chris "Noelle! Don't tell me you were bothering her."
    "He's kind of cute... are all the men in town like this?"
    holly "Um. I actually do need help... Do you know where the Jingle Bell Bakery is? I'm from out of town and I'm lost..."
    chris "hi"

    hide noelle
    hide chris

    #scene bg town 3
    #with fade

    "I got a hot chocolate - tis the season after all. It tastes delicious."
    "I'm walking around enjoying the sights. There's christmas lights and decorations everywhere you look- it's so magical!"
    "I'm enjoying the walk until a stranger smashes into me. My hot chocolate spills everywhere."
    felix "Hey! Look where you're going!"

    show felix
    "Now that I get a good look at him, he's so handsome...!"
    felix "Don't you know who I am?"
    "Wait, isn't he...?!"
    holly "hi"
    holly "You were the one who running!"
    felix "Well you should have moved! I have a train to catch."

    hide felix

    "he storms off."
    "I can't believe I'm this clumsy! I've done this twice today already."

    "I should probably get going. I need to keep driving to get to the big city."

    #scene bg town
    "Luckily I find my way back to my car."

    #scene bg road
    "As I'm going out I see someone on the side of the road."
    "wait... him again?!"
    show jack
    holly "Jack?! What are you doing here??"
    jack "Oh, Holly, right? Nice to see you again."
    jack "Bad news, you're going to have to turn back around. You can't come through here."
    holly "What?!"
    holly "But I need to pass through here! I need to get to the big city for a meeting!"
    nick "You're welcome to try. But a massive tree fell over on the road. Nobody can get through until after Christmas."
    holly "After Christmas?! So I'm gonna be stuck here for 5 days?!"
    nick "Sorry. But you can't pass."
    nick "But Mistletoe is a great town to get stuck in for Christmas!" #fix this line
    nick "I'll see you around."

    hide nick

    "He rode back towards town on his snowmobile."

    #scene bg town
    "Nick is right... It won't be so bad being in this town for Christmas!"
    "Oh, here's a hotel. I'll need to get a room!"

    #scene bg hotel lobby
    #with fade
    
    holly "What do you mean you don't have any rooms?!"
    hs "I'm sorry! Our rooms are always in demand at Christmas."
    holly "Well what am I supposed to do now?!"

    show felix
    with fade

    #felix bit

    


     
    







    






    return
