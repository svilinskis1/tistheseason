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

    "Christmas is the most magical time of year."
    "The snow, the decorations, the music..."
    "And time off work!"
    "I love my job in the city, but it's soooo boring sometimes."
    "They don't even let us decorate!"

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

    "I decided to drive. Who doesn't love a good Christmas roadtrip?"
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
    jack "There's a café called Jingle Bell Bakery just north of here." 
    jack "I know you wanted coffee, but they have the best hot chocolate in the state."
    holly "Well, thanks for the help."
    "That was SO awkward!"

    hide jack

    #scene bg town 2
    #with fade

    "Ugh, I'm lost! Where's this freakin bakery!"

    show noelle

    noelle "Hi lady! Are you lost?"
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
    chris "Oh, sure! It's just that way."
    holly "Thanks!"
    "This is so embarrassing... at least he's cute."

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
    "Oh... looks like it's starting to snow!"

    #scene bg road
    "I've barely gotten out of town and it's snowing hard."
    "At this rate I'll have to turn around. But I have to get to the meeting!"
    #the car crashes
    #tow truck comes
    "an old man steps out of the tow truck."
    #show santa
    "Old Man" "Do you need any help, ma'am?"
    holly "Yes!  I need towing!"
    "The old man starts attaching my car to his truck."
    "Old Man" "We'll have to go back to town. It's too dangerous to go farther til the snow stops."
    holly "As long as it's not out here!"
    "I climb into the passenger seat of the tow truck and we set off."
    "Old Man" "Unfortunately you'll have to stay in town for a few days. Our mechanic is out on vacation until after Christmas."
    holly "What kind of town only has one mechanic?"
    "Old Man" "We're a very small town."
    holly "I know! I'll call my fiancé and ask him to pick me up."
    "I dig my cell phone out of my jacket and call Kane. Luckily, he picks up."
    kane "Holly? What is it?"
    holly "Kane, can you come pick me up? I crached my car and now I'm stuck in this town called Mistletoe..."
    kane "Sure, Holly. I have a meeting tomorrow afternoon that I can't miss, so I'l drive over the day after that."
    "Does he think of anyhting except work?"
    holly "Are you sure you can't come earlier?"
    kane "Sorry Holly, you know how it is."
    holly "Well, thanks anyway. See you soon."
    "I hang up the phone."
    holly "What am I supposed to do until then?"
    "Old Man" "Stay a while! It's a beautiful place when you get to know it."
    "the truck stops. I open the door and get out."
    holly "Hey, where am I supposed to stay?"
    "Old Man" "Go to the center of town where the Christmas tree is. You'll find what you need there."
    "he drives off before I can ask what he means."
    

    #scene bg town
    "Oh, here's a hotel. I'll need to get a room!"

    #scene bg hotel lobby
    #with fade
    
    "As soon as I walk in, I see a familiar handsome face."
    "He sees me too."

    show felix
    with fade

    felix "You again!"
    holly "What are you doing here? I thought you had a train to catch!"
    felix "I missed it, because of you!"
    felix "I'm afraid you're too late, by the way. I've just gotten the last room."
    felix "Unless you want to share? "
    "What on earth does he mean by that?"
    holly "Nah"
            


    #felix bit

    


     
    







    






    return
