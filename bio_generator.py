
import random

def generate_bio(interests, creativity=0.85, length="medium", tone="professional"):
    """Generate relevant bios using curated templates"""
    
    if not interests or not interests.strip():
        interests = "lifestyle, creativity, inspiration"
    
    # Parse interests
    interest_list = [i.strip().lower() for i in interests.split(",") if i.strip()]
    
    # Bio templates by tone and length
    templates = {
        "professional": {
            "short": [
                f"{', '.join(interest_list[:2]).title()} enthusiast | Creating meaningful connections",
                f"Passionate about {', '.join(interest_list[:2])} | Let's connect!",
                f"{interest_list[0].title()} professional | Building the future",
                f"Dedicated to {', '.join(interest_list[:2])} | Making impact daily"
            ],
            "medium": [
                f"🌟 {', '.join(interest_list[:3]).title()} enthusiast\n💡 Sharing insights and inspiration\n📍 Building meaningful connections",
                f"✨ Passionate about {', '.join(interest_list[:2])}\n🚀 Creating positive impact\n💬 Always learning, always growing",
                f"🎯 {interest_list[0].title()} professional\n🌱 Focused on {', '.join(interest_list[1:3])}\n📧 Open to collaborations",
                f"💫 Living life through {', '.join(interest_list[:2])}\n🎨 Creative soul with purpose\n🤝 Let's connect and inspire!"
            ],
            "long": [
                f"🌟 Welcome to my corner of the internet!\n✨ Passionate about {', '.join(interest_list[:3])}\n💡 Sharing my journey and insights\n🚀 Always learning, always growing\n📍 Connect with me for collaborations",
                f"💫 {interest_list[0].title()} enthusiast | Life explorer\n🎨 Creating content around {', '.join(interest_list[1:3])}\n🌱 Believer in continuous growth\n💬 Love connecting with like-minded people\n📧 DM for partnerships!"
            ]
        },
        "casual": {
            "short": [
                f"Just here for the {', '.join(interest_list[:2])} ✨",
                f"{interest_list[0].title()} lover | Living my best life",
                f"Obsessed with {', '.join(interest_list[:2])} 💫",
                f"Here for good vibes and {interest_list[0]} 🌟"
            ],
            "medium": [
                f"✨ Living for {', '.join(interest_list[:2])}\n🌟 Good vibes only\n📸 Sharing my favorite moments",
                f"💫 {interest_list[0].title()} enthusiast\n🎨 Creating, exploring, enjoying\n🌈 Spreading positivity everywhere",
                f"🌟 Just a human who loves {', '.join(interest_list[:3])}\n✨ Capturing life's beautiful moments\n💛 Always down for adventures",
                f"💫 Passionate about {', '.join(interest_list[:2])}\n🎉 Living life to the fullest\n📱 Follow my journey!"
            ],
            "long": [
                f"✨ Hey there! Welcome to my little space\n🌟 Absolutely obsessed with {', '.join(interest_list[:3])}\n💫 Sharing all the good vibes and moments\n🎨 Always up for new adventures\n💛 Let's be friends and spread positivity!",
                f"🌈 Just your average {interest_list[0]} enthusiast\n✨ Living for {', '.join(interest_list[1:3])}\n💫 Documenting life's beautiful chaos\n🎉 Good energy attracts good people\n📱 Join me on this wild ride!"
            ]
        }
    }
    
    # Select appropriate template
    tone_templates = templates.get(tone, templates["professional"])
    length_templates = tone_templates.get(length, tone_templates["medium"])
    
    # Return random bio from appropriate category
    return random.choice(length_templates)
