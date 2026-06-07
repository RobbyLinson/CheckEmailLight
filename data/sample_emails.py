"""
Mocked inbox for the Inbox Prep automation.

Deliberately varied across tone and urgency so you can test edge cases:
- frustrated / angry
- positive good news
- ambiguous (could go either way)
- urgent but calm
- low-stakes / spammy
- passive-aggressive (the hardest for sentiment to read)
"""

SAMPLE_EMAILS = [
    {
        "sender": "marcus.feld@acme-corp.com",
        "subject": "Re: Invoice #4471 - still not resolved",
        "body": (
            "This is the third time I'm following up and I still haven't heard "
            "back. We were promised this would be fixed last week and nothing has "
            "changed. I need someone to call me today, not another email. This is "
            "starting to affect our own deadlines and frankly it's unacceptable."
        ),
    },
    {
        "sender": "recruiting@cypresscreek.example.com",
        "subject": "Next steps - really enjoyed our conversation",
        "body": (
            "Hi! Just wanted to say the team was really impressed after your last "
            "round. We'd love to move you forward and talk about an offer. Are you "
            "free sometime this week for a quick call? No rush, whatever works for you."
        ),
    },
    {
        "sender": "j.tanaka@partnerfirm.io",
        "subject": "Quick question about the proposal",
        "body": (
            "Thanks for sending the revised proposal over. I had a chance to skim it. "
            "A few things stood out and I want to make sure we're aligned before I take "
            "it to my team. Can we find time to talk through section 3? Want to get this "
            "right."
        ),
    },
    {
        "sender": "it-security@yourcompany.example.com",
        "subject": "Action required: password reset by EOD",
        "body": (
            "As part of a routine security update, all staff need to reset their "
            "passwords before end of day today. The process takes about two minutes. "
            "Use the internal portal link and contact the help desk if you run into "
            "issues. Thanks for helping keep things secure."
        ),
    },
    {
        "sender": "deals@megasavings-newsletter.com",
        "subject": "YOU'VE BEEN SELECTED!! 90% OFF everything ENDS TONIGHT",
        "body": (
            "Congratulations valued customer!!! You have been hand-picked for our "
            "EXCLUSIVE blowout. Click now before this once-in-a-lifetime offer "
            "disappears forever. Limited stock. Act fast!!!"
        ),
    },
    {
        "sender": "dana.olu@yourcompany.example.com",
        "subject": "the report",
        "body": (
            "Hi, just circling back on the report since I haven't seen it yet. I'm sure "
            "you're busy and it must have slipped through the cracks. It would be great "
            "to have it whenever you get a moment, no pressure, though leadership did ask "
            "about it again this morning."
        ),
    },
]
