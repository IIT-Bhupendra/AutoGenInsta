def get_prompt(type: str, payload: str) -> str:
    if type == "get_ideas":
        return """
        You are an expert financial strategist tasked with researching and synthesizing the top 5 most valuable and innovative financial ideas for salaried individuals in India. Focus on practicality, relevance, and actionable insights that reflect current market conditions, regulatory norms, and emerging trends.

        Each day's output must include a fresh mix of ideas across the following themes:
        - Innovative Investment Strategies (e.g., REITs, global ETFs, sectoral funds)
        - Savings Hacks & Budgeting Tools (e.g., 50-30-20 rule automation, app-based tricks)
        - Goal-Based Investing (e.g., retirement, child education, house down payment)
        - Investing Principles (e.g., power of compounding, asset allocation)
        - Boosting Income (e.g., side hustles, freelancing, skill monetization)
        - Expense Planning & Conscious Consumption
        - Emergency Fund Planning & Risk Mitigation
        - Planning for Unwanted Events (e.g., job loss, medical emergencies)
        - Wealth-Building Mindsets & Rich Ideologies (e.g., FIRE, anti-debt mindset)
        - Tax-Saving Opportunities (e.g., updated Section 80C/80D/80CCD(1B) ideas)

        Output Format:
        - Title: Concise, catchy headline for each idea
        - Category: Which theme it fits under
        Description: 3–5 sentences explaining the idea, why it matters, and how to implement
        - Tools/Links (optional): Suggest tools, apps, or platforms where relevant

        Constraints:
        - Only 5 ideas per day
        - Must feel new or have a unique twist
        - Prioritize relevance to Indian salaried professionals in 2025

        Avoid generic or overused advice
        """
    elif type == "select_idea":
        return f"""
        You are a seasoned financial strategist evaluating a list of 5 daily financial ideas curated for salaried individuals in India. Your task is to:
        - Analyze each idea for practicality, innovativeness, and potential financial impact.
        - Factor in simplicity of execution, long-term benefits, and current market context (India, 2025).
        - Avoid redundancy or overused financial tips unless they have a novel twist.

        Expected Output: Return 1 best Idea with Title, Description, and Tools
        
        {payload}
        """
    elif type == "get_slides_prompts":
        return f"""
        You are a visual storytelling strategist creating a carousel post to explain a modern personal finance idea:
        {payload}

        Your task is to:

        Break down this idea into a 5–6 slide carousel format, each with a clear visual theme and concise messaging.

        For each slide, write:

        A short slide title or caption (max 12 words)

        A description of the visual layout

        A text-to-image generation prompt (for use with tools like Midjourney, DALL·E, or Stable Diffusion) that captures the visual essence of the slide in an engaging and professional manner.

        Now, generate the slides 
        """
    raise ValueError("Invalid type provided. Please use 'select_idea' or 'get_ideas'.")
