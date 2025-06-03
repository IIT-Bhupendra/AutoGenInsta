from getprompt import get_prompt
from call_perplexity import call_perplexity

def main():
    # Step 1: Get the prompt for generating ideas
    prompt = get_prompt(type="get_ideas", payload="")
    
    # Step 2: Call Perplexity API to get ideas
    print("Generating ideas...")
    all_ideas = call_perplexity(prompt=prompt, model="sonar")
    
    # Step 3: Get the prompt for selecting the best idea
    selection_prompt = get_prompt(type="select_idea", payload=all_ideas)
    
    # Step 4: Call Perplexity API to select the best idea
    print("Selecting the best idea...")
    best_idea = call_perplexity(prompt=selection_prompt)
    
    # Step 5: Return the best idea
    # output = {"best_idea": best_idea}
    # print(output)
    # Write output to text file
    with open("output.txt", "w") as file:
        file.write(best_idea)
    print("Best idea written to output.txt")

    # Step 6: Get the prompt for generating slides
    print("Generating slides prompt...")
    slides_prompt = get_prompt(type="get_slides_prompts", payload=best_idea)
    slides_prompt_text = call_perplexity(prompt=slides_prompt, model="sonar")
    # Save the slides prompt to a text file
    with open("slides_prompt.txt", "w") as file:
        file.write(slides_prompt_text)

    # Send prompts to email
    from send_email import send_email
    send_email(
        subject="Daily Financial Ideas",
        body=f"Here are your daily financial ideas:\n\n{best_idea}\n\nSlides Prompt:\n{slides_prompt_text}",
        receiver_email="iitbhu.bhupendra@gmail.com"
    )

if __name__ == "__main__":
    main()
# This code is designed to run in a Python environment with the necessary libraries installed.