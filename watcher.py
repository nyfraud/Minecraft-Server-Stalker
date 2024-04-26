import requests
import json
import time

def get_server_status(server_address):
    try:
        response = requests.get(f"https://api.mcsrvstat.us/2/{server_address}")
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching server status:", e)
        return None

def send_to_discord(webhook_url, message):
    try:
        payload = {"content": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 204:
            print("Message sent to Discord successfully.")
        else:
            print(f"Failed to send message to Discord. Status code: {response.status_code}")
    except Exception as e:
        print("Error sending message to Discord:", e)

if __name__ == "__main__":
    # Replace these with your Minecraft server's IP address and Discord webhook URL
    server_address = ""   #server ip:port 
    webhook_url = ""   #webhookhere

    while True:
        server_status = get_server_status(server_address)
        if server_status:
            if server_status["online"]:
                message = f"Server is online with {server_status['players']['online']} players."
            else:
                message = "Server is offline."
        else:
            message = "Failed to fetch server status."

        send_to_discord(webhook_url, message)
        # Check server status every 5 minutes
        time.sleep(300)
