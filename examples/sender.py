import ldnlib

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="For a provided web resource, discover an ldp:inbox and POST the provided RDF to the receiver, if one exists")
    parser.add_argument("target", help="The IRI of the target web resource")
    parser.add_argument("filename", help="The filename of the JSON-LD message")
    parser.add_argument("--target_username", help="The username for the target resource")
    parser.add_argument("--target_password", help="The password for the target resource")
    parser.add_argument("--inbox_username", help="The username for the inbox resource")
    parser.add_argument("--inbox_password", help="The password for the inbox resource")
    parser.add_argument("--allow_local_inbox", type=bool, default=False, help="Whether to allow a local inbox address")

    args = parser.parse_args()

    target_auth = (args.target_username, args.target_password) if args.target_username and args.target_password else None
    inbox_auth = (args.inbox_username, args.inbox_password) if args.inbox_username and args.inbox_password else None

    sender = ldnlib.Sender(allow_localhost=args.allow_local_inbox)

    inbox = sender.discover(args.target, auth=target_auth)
    if inbox is not None:
        with open(args.filename, 'r') as f:
            sender.send(inbox, f.read(), auth=inbox_auth)
            print("Added message")
    else:
        print("Sorry, no inbox defined for the resource")

