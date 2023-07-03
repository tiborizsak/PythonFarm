import random
from datetime import datetime, timedelta

characters = [
    "Homer", "Marge", "Bart", "Lisa", "Maggie", "Moe", "Lenny", "Carl", "NedFlanders",
    "PrincipalSkinner", "Barney", "Krusty", "MrBurns", "Smithers", "Milhouse", "RalphWiggum",
    "ChiefWiggum", "Nelson", "EdnaKrabappel", "SideshowBob", "Apu", "KentBrockman", "ComicBookGuy", "Otto"
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
    "NedFlanders": "Hi-diddly-ho, neighborino!",
    "PrincipalSkinner": "No, mother, it’s just the Northern Lights.",
    "Barney": "It begins!",
    "Krusty": "Hey hey!",
    "MrBurns": "Excellent.",
    "Smithers": "But sir...",
    "Milhouse": "Everything’s coming up Milhouse!",
    "RalphWiggum": "I'm special!",
    "ChiefWiggum": "Nothing to see here.",
    "Nelson": "Ha-ha!",
    "EdnaKrabappel": "Ha!",
    "SideshowBob": "Hello, Bart.",
    "Apu": "Thank you, come again.",
    "KentBrockman": "This just in!",
    "ComicBookGuy": "Worst. Episode. Ever.",
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
        log_line_len = len(log_line)
        f.write(str(log_line_len) + " " + log_line)

        timestamp += timedelta(seconds=1)
