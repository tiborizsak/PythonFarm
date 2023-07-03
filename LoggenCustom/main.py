import random
from datetime import datetime, timedelta

characters = [
    "Homer", "Marge", "Bart", "Lisa", "Maggie", "Moe", "Lenny", "Carl", "Ned Flanders",
    "Principal Skinner", "Barney", "Krusty", "Mr. Burns", "Smithers", "Milhouse", "Ralph Wiggum",
    "Chief Wiggum", "Nelson", "Edna Krabappel", "Sideshow Bob", "Apu", "Kent Brockman", "Comic Book Guy", "Otto"
]

quotes = {
    "Homer": "Mmm... donuts.",
    "Marge": "I just think they're neat.",
    "Bart": "I didn’t do it.",
    "Lisa": "If anyone wants me, I’ll be in my room.",
    "Maggie": "*suck* *suck*",
    "Moe": "Why don't you smash the chair on my head?",
    "Lenny": "Ow! My eye!",
    "Carl": "So, what do you think of the girls?",
    "Ned Flanders": "Hi-diddly-ho, neighborino!",
    "Principal Skinner": "No, mother, it’s just the Northern Lights.",
    "Barney": "It begins!",
    "Krusty": "Hey hey!",
    "Mr. Burns": "Excellent.",
    "Smithers": "But sir...",
    "Milhouse": "Everything’s coming up Milhouse!",
    "Ralph Wiggum": "I'm special!",
    "Chief Wiggum": "Nothing to see here.",
    "Nelson": "Ha-ha!",
    "Edna Krabappel": "Ha!",
    "Sideshow Bob": "Hello, Bart.",
    "Apu": "Thank you, come again.",
    "Kent Brockman": "This just in!",
    "Comic Book Guy": "Worst. Episode. Ever.",
    "Otto": "Rock on, dude!"
}

fruits = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango",
    "nectarine", "orange", "papaya", "raspberry", "strawberry", "tangerine", "watermelon", "blueberry",
    "coconut", "blackberry", "pear", "peach", "plum", "pomegranate", "pineapple"
]

apps = ["sshd", "httpd", "mysqld", "syslog", "smtpd", "vsftpd", "dhcpd", "cupsd", "crond", "atd", "postfix", "exim",
        "dovecot", "named", "iptables"]

# RFC5424 Syslog facilities
facilities = list(range(0, 24))
severities = list(range(0, 8))

timestamp = datetime(2041, 6, 10)

with open('customIETF.log', 'w') as f:
    for i in range(20000):
        priority = (random.choice(facilities) * 8) + random.choice(severities)
        host = random.choice(characters)
        facility = "user"
        app_name = random.choice(apps)
        procid = random.randint(1000, 9999)
        msgid = "MSG" + str(random.randint(100, 999))
        message = f'q="{quotes[host]}",f={random.choice(fruits)}'
        structured_data = "-"

        log_line = f'<{priority}>1 {timestamp.isoformat()} {host} {app_name} {procid} {msgid} {structured_data} {message}\n'
        f.write(log_line)

        timestamp += timedelta(seconds=1)
