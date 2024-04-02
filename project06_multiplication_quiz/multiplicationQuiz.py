import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers 0-9
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt,
                      allowRegexes=['^%s$' % (num1 * num2)], # only allow correct answer
                      blockRegexes=[('.*', 'Incorrect!')],  # blocks all input, except allowRegexes
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)  # Brief pause to let user see the result.
    print('0Score: %s / %s\n' % (correctAnswers, numberOfQuestions))