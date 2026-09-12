#opensource sc to create a file from facebook user followers
#save formate uid|name


import re
import requests
import random
import json,os
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','dpr': '1.125','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="152", "Not?A_Brand";v="24", "Google Chrome";v="152"','sec-ch-ua-full-version-list': '"Chromium";v="152.0.7977.76", "Not?A_Brand";v="24.0.0.0", "Google Chrome";v="152.0.7977.76"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"19.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36','viewport-width': '924',}


def GetData(req):
    try:
        av = re.search(r'"actorID":"(.*?)"', str(req)).group(1)
        __user = av
        __a = str(random.randrange(1, 6))
        __hs = re.search(r'"haste_session":"(.*?)"', str(req)).group(1)
        __ccg = re.search(r'"connectionClass":"(.*?)"', str(req)).group(1)
        __rev = re.search(r'"__spin_r":(.*?),', str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search(r'"__spin_b":"(.*?)"', str(req)).group(1)
        __spin_t = re.search(r'"__spin_t":(.*?),', str(req)).group(1)
        __hsi = re.search(r'"hsi":"(.*?)"', str(req)).group(1)
        fb_dtsg = re.search(
            r'"DTSGInitialData",\[\],{"token":"(.*?)"}',
            str(req)
        ).group(1)
        jazoest = re.search(r'jazoest=(.*?)"', str(req)).group(1)
        lsd = re.search(
            r'"LSD",\[\],{"token":"(.*?)"}',
            str(req)
        ).group(1)
        return {
            'av': av,
            '__user': __user,
            '__a': __a,
            '__hs': __hs,
            'dpr': '1.5',
            '__ccg': __ccg,
            '__rev': __rev,
            '__spin_r': __spin_r,
            '__spin_b': __spin_b,
            '__spin_t': __spin_t,
            '__hsi': __hsi,
            '__comet_req': '15',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd
        }
    except Exception:
        return {}



def get_followers(uid,data,ck,filename):
    response = requests.get('https://www.facebook.com/61594069678342', cookies={"cookie":ck}, headers=headers)
    data = GetData(response.text)
    #print(data)
    req2 = requests.get(f"https://www.facebook.com/{uid}/followers",cookies={"cookie":ck}, headers=headers)
    end_cursor = re.search(r'"end_cursor":"(.*?)"',str(req2.text)).group(1)
    cltoken = re.search(r'"collectionToken":"(.*?)"',str(req2.text)).group(1)
    #print(end_cursor)
    results = []
    while end_cursor:
    
        data.update({
            '__crn': 'comet.fbweb.CometProfileFollowersTabRoute',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfileCometAppCollectionListRendererPaginationQuery',
            'server_timestamps': 'true',
            'variables': json.dumps({
                'count': 8,
                'cursor': end_cursor,
                'scale': 1,
                'search': None,
                'id':cltoken,
                '__relay_internal__pv__FBProfile_enable_perf_improv_gkrelayprovider': True
            }),
            'doc_id': '26157687557261750'
        })
        datax = requests.post('https://www.facebook.com/api/graphql/', cookies={"cookie":ck}, headers=headers, data=data).json()
        edges = datax["data"]["node"]["pageItems"]["edges"]
        end = datax["data"]["node"]["pageItems"]["page_info"]["end_cursor"]
        for item in edges:
            node = item.get("node", {})
            name = node.get("title", {}).get("text")
            uid = node.get("node", {}).get("id")

            if name and uid:
                results.append({"uid": uid,"name": name})
                with open(filename,"a",encoding="utf-8") as f:
                    f.write(uid + "|" + name + "\n")
                print(uid,name)
        end_cursor=end

    return results



def friend():
    os.system("cls")
    print(49*'-')
    print("              File Create Fb0.1 - Xerx")
    print(49*'-')
    start_uid = input(" Enter Public uid or username =  ")
    print(49*'-')
    ck = input(" Enter Fresh Cookie = ")
    print(49*'-')
    filename = input(" Enter File Name = ")
    response = requests.get('https://www.facebook.com/61594069678342', cookies={"cookie":ck}, headers=headers)
    data = GetData(response.text)

    #print(data)
    uids = [start_uid]
    processed = set()
    i=0
    

    while i < len(uids):

        current_uid = uids[i]
        if current_uid in processed:
            i += 1
            continue
        print(49*'-')
        print("Processing:", current_uid)
        print(49*'-')
        processed.add(current_uid)
        followers = get_followers(current_uid,data,ck,filename)
        #print(followers)
        for user in followers:
            uid = user["uid"]
            name = user["name"]
            print(uid, "=>", name)
            
            if uid not in processed and uid not in uids:
                uids.append(uid)
        i += 1
        print("Total ids:", len(uids))

friend()
