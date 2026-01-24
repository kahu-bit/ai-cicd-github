from google import genai
import sys

client = genai.Client()

# Define a function that takes a code diff as input
def review_code(diff_text):

    # Write a multi-line f-string prompt that includes {diff_text}
    # Tell Gemini to act as a code reviewer and focus on security, bugs, performance
    prompt = f"""You are an expert code reviewer. Review the following code diff and provide feedback.

        Focus on:
        1. Security vulnerabilities
        2. Bug risks
        3. Performance issues
        4. Best practice violations

        # Ask for Severity (HIGH/MEDIUM/LOW), Description,
        # and Suggested fix per issue
        Determine severity level (HIGH/MEDIUM/LOW) of the issue and suggest a fix each issue

        If the code looks good, say so.

        # Tell Gemini to end with exactly: SEVERITY_SUMMARY: <level>
        # Rules: CRITICAL = any HIGH issues, WARNING = MEDIUM/LOW only, 
        # GOOD = no issues
        End with SEVERITY_SUMMARY: Critical: HIGH issues, WARNING = MEDIUM/LOW, GOOD = no issues

        Code diff to review:

        # Use f-string syntax to insert the diff_text variable
        {diff_text}

        Provide your review in a clear, structured format, ending with the SEVERITY_SUMMARY line."""


    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=diff_content
    )

    # Return just the text from the response
    return response.text 

def parse_severity(review_text):
    """Extract severity level from the review output."""
    for line in review_text.strip().split("\n"):
        if line.strip().startswith("SEVERITY_SUMMARY:"):
            level = line.split(":", 1)[1].strip().upper()
            if level in ("CRITICAL", "WARNING", "GOOD"):
                return level
    return "WARNING"  # Default to WARNING if parsing fails

 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()

    review = review_code(diff_content)
    severity = parse_severity(review)

    # Print review to stdout (for the PR comment)
    print(review)

    # Write severity to a file (for the labeling step)
    with open("severity.txt", "w") as f:
        f.write(severity)





