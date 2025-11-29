"""
✨ SPECIAL SURPRISE - DO NOT OPEN UNTIL YOU COMPLETE EXERCISE 1! ✨

Run this file after completing your first Python exercise.
Command: python congratulations.py
"""

import time
import sys

def typewriter_effect(text, delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(char="=", length=60):
    """Print decorative border"""
    print(char * length)

def display_message():
    """Display special congratulations message from Sergio"""
    
    # Clear and create suspense
    print("\n" * 3)
    time.sleep(0.5)
    
    # Header
    print_border("✨")
    print()
    typewriter_effect("🎉 CONGRATULATIONS MAURICIO! 🎉", 0.03)
    print()
    print_border("✨")
    print()
    time.sleep(1)
    
    # Personal message
    typewriter_effect("A Personal Message from Your Father:", 0.04)
    print()
    time.sleep(0.5)
    
    message = """
Dear Mauricio,

You just completed your FIRST Python exercise!

I am SO incredibly proud of you, son.

While you're in Brussels doing amazing work at PE Club, you're ALSO 
finding time to learn new technical skills. That dedication and drive 
is what makes you exceptional.

This is just the beginning. Every function you write, every model you 
build, every line of code you complete - you're becoming more powerful.

You're not just a Private Equity analyst anymore.
You're becoming a TECHNICAL Private Equity analyst.

That combination is RARE. That combination is VALUABLE.
That combination will take you to the top.

Remember:
- PE Club was lucky to get you
- Brussels is just your current chapter
- The world is yours to conquer
- Your father believes in you completely

Keep going. Keep learning. Keep growing.

The best is yet to come.

With all my love, pride, and admiration,

Papá

P.S. - When you complete your first DCF model, there's another 
surprise waiting... 😉

---

Sergio Muñoz de Alba Medrano
November 2025
México → Brussels → The World 🌍
    """
    
    for line in message.split('\n'):
        typewriter_effect(line, 0.02)
        time.sleep(0.1)
    
    print()
    print_border("✨")
    print()
    
    # Celebration
    time.sleep(1)
    celebration = [
        "🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉",
        "   ¡VAMOS MAURICIO!",
        "🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉 🎊 🎉"
    ]
    
    for line in celebration:
        print(line.center(60))
        time.sleep(0.3)
    
    print()
    print_border("✨")
    print()
    
    # Statistics
    time.sleep(1)
    stats = """
📊 YOUR PROGRESS:
------------------
✅ Python Environment: SETUP COMPLETE
✅ First Exercise: COMPLETED
✅ Lines of Code Written: 50+
✅ Father's Pride Level: MAXIMUM! 💪

🎯 NEXT MILESTONES:
-------------------
→ Complete Module 2 (Python Fundamentals)
→ Build first financial calculator
→ Learn Pandas for data analysis
→ Create first DCF model
→ Master GitHub workflow

💎 SKILLS UNLOCKED:
-------------------
▪ Python basics ✨
▪ Variables & data types
▪ Functions
▪ Financial calculations
▪ Problem-solving mindset

Keep going! The next challenge awaits! 🚀
    """
    
    print(stats)
    print()
    print_border("=")
    print()
    
    # Final message
    typewriter_effect("Now get back to learning... but know that your father is smiling! 😊", 0.03)
    print()
    time.sleep(0.5)
    
    typewriter_effect("P.S. - Don't forget to subscribe to GitHub Copilot! It gets MUCH easier! 💡", 0.03)
    print()
    print_border("=")
    print()

if __name__ == "__main__":
    # Check if running in terminal
    try:
        display_message()
        
        # Save completion
        with open('first_exercise_completed.txt', 'w') as f:
            f.write(f"Mauricio completed his first exercise!\n")
            f.write(f"Date: {time.strftime('%B %d, %Y at %I:%M %p')}\n")
            f.write(f"\nMessage from Sergio: So proud of you, son! ❤️\n")
        
        print("💾 A special memory has been saved: 'first_exercise_completed.txt'")
        print()
        
    except KeyboardInterrupt:
        print("\n\nNo problem! Run this again when you're ready! 🎉")
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        print("But your father is still proud of you! ❤️")
