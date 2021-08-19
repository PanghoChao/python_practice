def std_weight(height, gender):
    
    if gender == "남자":
        weight = height*height*22

        return weight/10000
    else :
        weight = height*height*21
        
        return weight/10000

height = 175
gender ="여자"
weight = std_weight(height, gender) 
weight = round(weight,2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) 
