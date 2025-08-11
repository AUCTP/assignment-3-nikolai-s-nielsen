## Task 1 ##

data = {
    "Mike": {
        "salesTarget": 130,
        "customerSatisfaction": 5,
        "attendance": 23,
        "peerFeedback": 3
    }
}

def evaluate_performance(data):
    data2 = []
    for employee in data:
        if data[employee]['salesTarget'] > 120:
            data2.append("excellent")
        elif 100 <= data[employee]['salesTarget'] <= 120:
            data2.append('good')
        elif 80 <= data[employee]['salesTarget'] < 100:
            data2.append('average')
        elif data[employee]['salesTarget'] < 80:
            data2.append('poor')
    
        if data[employee]['customerSatisfaction'] < 6:
            data2.append('poor')
        elif 6 <= data[employee]['customerSatisfaction'] <= 7:
            data2.append('average')
        elif 8 <= data[employee]['customerSatisfaction'] <= 9:
            data2.append('good')
        elif data[employee]['customerSatisfaction'] == 10:
            data2.append('excellent')

        if data[employee]['attendance'] < 20:
            data2.append('poor')
        elif 20 <= data[employee]['attendance'] <= 24:
            data2.append('average')
        elif 25 <= data[employee]['attendance'] <= 27:
            data2.append('good')
        elif data[employee]['attendance'] >= 28:
            data2.append('excellent')
        
        if data[employee]['peerFeedback'] < 4:
            data2.append('poor')
        elif 4 <= data[employee]['peerFeedback'] <= 6:
            data2.append('average')
        elif 7 <= data[employee]['peerFeedback'] <= 8:
            data2.append('good')
        elif 9 <= data[employee]['peerFeedback'] <= 10:
            data2.append('excellent')

        if data2.count("excellent") == 4:
            return 'Outstanding'
        elif data2.count('poor') == 2:
            return 'Needs Improvement'
        elif data2.count('good') == 3:
            return 'Strong Performer'
        else:
            return'Satisfactory'

perform = evaluate_performance(data)
print(f'Performance is {perform}')

performance = evaluate_performance(data)

data3 = {
    "Mike": {
        "performanceRating": performance,
        "yearsOfService": 6
    }
    }

def calculate_bonus(data3):
    data4 = []
    for employee in data:
        if data3[employee]['performanceRating'] == 'Outstanding':
            data4.append(1000)
        elif data3[employee]['performanceRating'] == 'Strong Performer':
            data4.append(800)
        elif data3[employee]['performanceRating'] == 'Satisfactory':
            data4.append(500)
        elif data3[employee]['performanceRating'] == 'Needs Improvement':
            data4.append(200)
        
        number = sum(data4)

        if data3[employee]['yearsOfService'] < 2:
            return number * 1
        elif 2 <= data3[employee]['yearsOfService'] <= 5:
            return number * 1.5
        elif data3[employee]['yearsOfService'] > 5:
            return number * 2

bonusYear = calculate_bonus(data3)
print(f'Annual bonus is ${bonusYear}')


