def main():
    client_file = open('clients.txt','r')
    
    for c in client_file:
        client = c.rstrip('\n')

        print(client)

    client_file.close()

main()