
import subprocess
import optparse
import multiprocessing
import time

start_time = time.time()



def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-d", "--domain",dest="domain",help="target domain")
    return parse_object.parse_args()


def run_dnsrecon(domain):
    try:
        print("-------------------Runnig DNSRecon-------------------")
        result = subprocess.run(["dnsrecon","-d", domain],stdout=subprocess.PIPE,stderr=subprocess.PIPE, check=True)
        print(result.stdout.decode())
        print("----------------------Ending Result DNSRecon----------------------")
    except:
        print(result.stderr.decode())

def run_sublist3r(domain):
    try:
        print("-------------------Running Sublist3r-------------------")
        result =subprocess.run(["sublist3r","-d",domain],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
        print(result.stdout.decode())
        print("----------------------Ending Result Sublist3r----------------------")
    except:
        print(result.stderr.decode())

def run_whois(domain):
    try:
        print("-------------------Runinnig Whois------------------")
        result =subprocess.run(["whois",domain],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
        print(result.stdout.decode())
        print("----------------------Ending Result Whois----------------------")
    except:
        print(result.stderr.decode())

def main():
    (user_inputs,arguments) = get_user_input()
    p1 = multiprocessing.Process(target=run_dnsrecon,args=(user_inputs.domain,))
    p2 = multiprocessing.Process(target=run_sublist3r,args=(user_inputs.domain,))
    p3 = multiprocessing.Process(target=run_whois,args=(user_inputs.domain,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

   
if __name__=="__main__":
    main()
    print("--- Total time: %s seconds ---" % (time.time() - start_time))
