# input : name: 'ali', age: 18 , scores= [14,15,16,12,10,20]
# output : Ali (18), passed 4 courses

PASSED_SCORE = 12

def announce(name, age, scores):
    passed = 0
    for score in scores:
        if score > PASSED_SCORE:
            passed += 1
    return f"{name} \t ({age}), \t passed {passed} courses "