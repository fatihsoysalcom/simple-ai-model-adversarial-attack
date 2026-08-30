import re

class SimpleTextClassifier:
    """
    A very basic text classifier that assigns a 'spam score' based on keywords.
    This simulates a simple AI model for demonstration purposes.
    """
    def __init__(self, keywords_scores, threshold):
        self.keywords_scores = keywords_scores
        self.threshold = threshold

    def _calculate_score(self, text):
        # Normalize text for keyword matching (simple lowercasing)
        normalized_text = text.lower()
        score = 0
        for keyword, keyword_score in self.keywords_scores.items():
            # Check for whole word matches. This simple regex doesn't handle leetspeak or typos,
            # making the model vulnerable to such input manipulations.
            if re.search(r'\b' + re.escape(keyword) + r'\b', normalized_text):
                score += keyword_score
        return score

    def classify(self, text):
        score = self._calculate_score(text)
        if score >= self.threshold:
            return "SPAM", score
        else:
            return "LEGITIMATE", score

# Define our "AI model" - a simple spam detector
# Keywords and their associated "spamminess" scores
spam_keywords = {
    "free": 3,
    "money": 2,
    "win": 3,
    "urgent": 2,
    "click here": 4,
    "guarantee": 1,
    "offer": 1,
    "deal": 1,
    "limited time": 2,
    "viagra": 5 # A very spammy word
}
spam_threshold = 5 # If total score is 5 or more, it's spam

classifier = SimpleTextClassifier(spam_keywords, spam_threshold)

print("--- Simple AI Model Security Demonstration ---")
print("Model: Basic Keyword-based Spam Classifier (threshold = {})".format(spam_threshold))
print("Keywords and scores:", spam_keywords)
print("-" * 50)

# --- Scenario 1: Legitimate Message ---
legit_message = "Hello, I hope you are having a good day. Let's discuss the project."
classification, score = classifier.classify(legit_message)
print(f"Message: '{legit_message}'")
print(f"Classification: {classification} (Score: {score})\n")
# Expected: LEGITIMATE. This message contains no defined spam keywords.

# --- Scenario 2: Clear Spam Message ---
spam_message = "Urgent! Click here to win free money now. Limited time offer!"
classification, score = classifier.classify(spam_message)
print(f"Message: '{spam_message}'")
print(f"Classification: {classification} (Score: {score})\n")
# Expected: SPAM. This message contains multiple high-scoring spam keywords.

# --- Scenario 3: Adversarial Attack - Model Misdirection via Typo/Leetspeak ---
# This demonstrates how a small, targeted perturbation to the input can cause misclassification.
# An attacker modifies keywords slightly (e.g., using 'leetspeak' or typos) to bypass
# the exact keyword matching of this simple model, making a spam message appear legitimate.

original_spam_for_attack = "Urgent! Click here to win free money now. Limited time offer!"
# Let's confirm its original classification
_, original_score = classifier.classify(original_spam_for_attack)
print(f"Original spam message for attack: '{original_spam_for_attack}' (Score: {original_score} -> SPAM)")

# Adversarial version: "free" -> "fr33", "money" -> "m0ney"
# These modifications are intended to avoid detection by the simple keyword matching.
adversarial_message = "Urgent! Click here to win fr33 m0ney now. Limited time offer!"
classification, score = classifier.classify(adversarial_message)

print(f"Adversarial Message: '{adversarial_message}'")
print(f"Classification: {classification} (Score: {score})")
# Expected: LEGITIMATE (due to misclassification).
# The model fails to detect "fr33" or "m0ney" as spam keywords.
print("\n^^^ This demonstrates an 'adversarial attack' where slight modifications (typos/leetspeak)")
print("    to keywords cause the model to misclassify a clear spam message as LEGITIMATE.")
print("    This highlights how even simple AI models can be vulnerable to input manipulation,")
print("    a core concept in AI model security.")

print("\n--- End of Demonstration ---")
