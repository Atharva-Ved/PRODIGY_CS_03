# PRODIGY_CS_03

Task-03 : Password Complexity Checker
PROBLEM STATEMENT: Build a tool that assesses the strength of a password 
based on criteria such as length, presence of uppercase 
and lowercase letters, numbers, and special characters. 
Provide feedback to users on the password's strength

VIDEO LINK => https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22index.html%20-%20task3%20-%20Visual%20Studio%20Code%202025-01-10%2000-41-06.mp4%22%2C%22type%22%3A%22video%2Fmp4%22%2C%22signedurl_expire%22%3A%222028-01-09T19%3A52%3A20.105Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2Fa596210abbbb4460%2Findex.html%2520-%2520task3%2520-%2520Visual%2520Studio%2520Code%25202025-01-10%252000-41-06.mp4%3FExpires%3D1831060340%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DaZLit8qqPWG6ZP0D-3dTKFwgnPo6JC6JLfCdmJ3Hgq-TEAUIvbjFYK1Tq0o2b19kv9mx~xfFtKSdst6Xe6G2-u3OBZwcqbnHe97EtzGk93q1utuXsE4v-bxWKEqK25bbGNv1zxOibSiv7O8lwPM5Nk2WOyl77NpwWpmhd9DL03fsez00Ce~P56tSQq~7tJHEvvgCPUZYHjFO6cAAXuiZubJkmBiRtNjXcino4I9-6Fdq8A23WrgU76kMsx8xd5j8ZDkbfXo1HzSdo52gYp6-cJ3VppfDCJZ-EHMGYLjPpu~qGmEOfvZeYqLCwtP3zu2VJHEs1Wu97AlbYh6Kq7gtGg__%22%7D

The one with app.py is GUI BASED and one with pcc.py is CLI BASED.

Problem Statement Overview: The goal is to develop a tool that evaluates the strength of a password based on specific criteria. The tool will provide feedback on whether the password meets various security requirements and give users recommendations for improving it.
How the Password Complexity Checker Works:

  Password Strength Criteria: A strong password generally needs to meet the following criteria:
        Length: The password should be long enough to resist brute force attacks. A good password should typically be at least 8-12 characters long.
        Uppercase Letters: The password should contain at least one uppercase letter (A-Z).
        Lowercase Letters: The password should include at least one lowercase letter (a-z).
        Numbers: The password should include at least one number (0-9).
        Special Characters: It should contain at least one special character (e.g., !, @, #, $, %, &, etc.).

  These criteria are common requirements for many security systems, aiming to ensure that the password is not easy to guess or crack.

  Password Strength Assessment:
        The tool will evaluate the password based on the above criteria and return a strength rating (e.g., weak, moderate, strong) with specific feedback.
        The tool could also provide suggestions for improving the password if it does not meet certain criteria.

   User Feedback:
        Weak Password: If the password is short and/or lacks diversity in characters (e.g., no uppercase letters, numbers, or special characters).
        Moderate Password: If the password meets some of the requirements but could be improved (e.g., lacks one of the essential elements, like a special character).
        Strong Password: If the password meets all the criteria, making it difficult to guess or crack.

   The tool will provide feedback on which criteria are missing or need improvement.

  Example Use Case for the Tool:
        Step 1: The user enters a password in a text box.
        Step 2: The tool evaluates the password based on the criteria mentioned above.
        Step 3: The tool provides feedback, such as:
            "Password too short. Consider adding more characters."
            "Missing uppercase letters. Add at least one."
            "Your password is strong!"
        Step 4: If the password does not meet certain criteria, the tool will suggest changes (e.g., adding special characters, mixing upper and lowercase letters, etc.).
        Step 5: The user is given the option to re-enter a stronger password or accept the feedback.

Key Features of the Tool:

   Length Check:
        The password should have a minimum length (e.g., 8 characters) to avoid weak passwords.
        Passwords shorter than the required length should trigger feedback advising the user to increase the length.

  Character Variety Check:
      The tool checks whether the password includes:
        Uppercase Letters: If no uppercase letters are found, feedback should recommend adding at least one.
        Lowercase Letters: If no lowercase letters are found, feedback should suggest adding at least one.
        Numbers: If no numbers are present, feedback should encourage adding numeric digits.
        Special Characters: If no special characters are present, feedback should suggest using symbols like !, @, or #.

  Password Strength Rating:
       Based on the number of criteria met, the tool will assign a strength rating (e.g., Weak, Moderate, Strong).
       Weak: Password fails to meet at least three criteria.
       Moderate: Password meets some criteria but lacks key elements.
       Strong: Password meets all criteria (sufficient length, uppercase, lowercase, number, and special character).

   Security Recommendations:
       Provide real-time feedback during password entry, highlighting which specific requirements are unmet (e.g., “Password is missing special characters!”).
       Offer suggestions for improvement, such as adding uppercase letters or increasing the length of the password.

  User-Friendly Interface:
       A simple, intuitive interface where users can type in a password and immediately receive feedback.
       A progress bar or strength meter can be displayed to visualize password strength (e.g., red for weak, yellow for moderate, green for strong).

Example Scenarios and Feedback:

   Scenario 1 (Weak Password):
       Password: 12345
       Feedback: "Password too short. Add at least 3 more characters. Missing uppercase letters, special characters, and lowercase letters."

   Scenario 2 (Moderate Password):
      Password: Password123
      Feedback: "Good length, but consider adding special characters to make it stronger."

  Scenario 3 (Strong Password):
     Password: P@ssw0rd!2025
     Feedback: "Strong password! Your password meets all the requirements."

Security Considerations:

  Avoiding Common Passwords: The tool could provide feedback to help users avoid using easily guessable or common passwords (e.g., password123, 123456, etc.). These passwords can be checked against known breached password lists to improve security.
  Feedback Based on Modern Standards: As password security standards evolve (e.g., NIST guidelines), the password checker should be updated to reflect current best practices.

Example Use Cases and Tools for User Interaction:

  CLI-Based Password Checker:
      The user enters a password in the terminal, and the tool evaluates and prints out feedback (similar to the previous CLI-based Caesar Cipher example).
  GUI-Based Password Checker (e.g., using tkinter):
      The user enters a password in a text box.
      The program provides visual feedback, such as a color-coded strength bar or a set of text indicators that show which criteria have been met or not met.

Conclusion:

A Password Complexity Checker is an essential tool for enhancing security by helping users create strong, resilient passwords. By evaluating passwords based on length, character variety, and overall complexity, the tool can guide users to adopt better password practices and protect themselves from common security risks, such as brute force attacks and credential stuffing.

Such a tool is widely used in websites, applications, and security systems to ensure users are following safe password practices. This tool will be a valuable addition to your GitHub repository, showcasing your skills in security, user feedback, and Python development.
