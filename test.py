import requests

def send_requests(base_url, keywords):
    result = []
    success = 0
    failed = 0
    for i in range(len(keywords)):
        url = f"{base_url}?keyword={keywords[i]}"
        response = requests.get(url)
        
        if response.status_code == 200:
            result.append(response.text)
            success+=1
        else:
            result.append(f"Request {i + 1}: Failed - Status Code: {response.status_code}")
            failed+=1
            
    print(result)
    print(str(len(result))+'중 성공률'+str(len(result)/success))
    return result

if __name__ == "__main__":
    base_url = "http://localhost:8001/search/"
    keyword = ["단어",'카페인','함장','합참','군대','양구','포스코','취업','청창사','사과','바나나','포도','호박','파인애플','근두운','두음법칙']

    send_requests(base_url, keyword)
