from utils.image_analysis import analyze_image
import random

def generate_instagram_captions(image, creativity=0.85, style="Default", language="English", num_captions=3):
    # Get image description using BLIP
    description = analyze_image(image)
    
    # Create Instagram-style captions using templates
    captions = create_instagram_style_captions(description, style, num_captions)
    
    # Translate if needed
    if language.lower() != "english":
        captions = translate_captions(captions, language)
    
    return captions

def create_instagram_style_captions(description, style, num_captions):
    """Convert description to Instagram-style captions using templates"""
    
    # Extract key elements from description
    description_clean = description.lower().strip()
    
    templates = {
        "Default": [
            f"Loving this moment! ✨ {description}",
            f"Can't get enough of this view 📸 {description}",
            f"Perfect day for this! {description}",
            f"Feeling grateful ✨ {description}",
            f"Just wow! {description} 🌟",
            f"Living for moments like these ✨ {description}",
            f"Nature's beauty never ceases to amaze 🌙 {description}",
            f"Peaceful vibes ✨ {description}"
        ],
        "Funny": [
            f"When the universe decides to show off 😂 {description}",
            f"Me trying to be aesthetic: {description} 🤪",
            f"Plot twist: this wasn't planned! {description}",
            f"Accidentally took the perfect shot 📸 {description}",
            f"Nature said 'hold my beer' 😅 {description}"
        ],
        "Motivational": [
            f"Every sunset brings the promise of a new dawn 🌅 {description}",
            f"Find beauty in every moment ✨ {description}",
            f"Dream big, shine bright! {description} 💫",
            f"Life is beautiful when you take time to notice 🌟 {description}",
            f"Chase your dreams under every sky ✨ {description}"
        ],
        "Minimalist": [
            f"{description} ✨",
            f"Simply beautiful. {description}",
            f"Tonight. {description}",
            f"{description}.",
            f"Pure magic ✨ {description}"
        ],
        "Question": [
            f"Isn't this view just perfect? {description}",
            f"Who else loves moments like these? {description}",
            f"Can you feel the magic? ✨ {description}",
            f"What's your favorite time of day? {description}",
            f"Doesn't this take your breath away? {description}"
        ]
    }
    
    style_templates = templates.get(style, templates["Default"])
    selected_templates = random.sample(style_templates, min(num_captions, len(style_templates)))
    
    return selected_templates

def translate_captions(captions, target_language):
    """Simple translation using transformers"""
    try:
        from transformers import pipeline
        
        lang_codes = {
            "spanish": "en-es",
            "french": "en-fr", 
            "german": "en-de",
            "hindi": "en-hi"
        }
        
        if target_language.lower() in lang_codes:
            model_name = f"Helsinki-NLP/opus-mt-{lang_codes[target_language.lower()]}"
            translator = pipeline("translation", model=model_name)
            
            translated = []
            for caption in captions:
                try:
                    result = translator(caption, max_length=100)[0]['translation_text']
                    translated.append(result)
                except:
                    translated.append(caption)  # Fallback to original
            return translated
        
    except Exception as e:
        print(f"Translation failed: {e}")
    
    return captions  # Return original if translation fails