import ldnlib

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="""For a provided web
        resource, discover an ldp:inbox and GET the notifications from
        that inbox, if one exists""")
    parser.add_argument("target", help="The IRI of the target web resource")
    parser.add_argument("--target_username",
                        help="The username for the target resource")
    parser.add_argument("--target_password",
                        help="The password for the target resource")
    parser.add_argument("--inbox_username",
                        help="The username for the inbox resource")
    parser.add_argument("--inbox_password",
                        help="The password for the inbox resource")
    parser.add_argument("--allow_local_inbox", type=bool, default=False,
                        help="Whether to allow a local inbox address")

    args = parser.parse_args()

    target_auth = None
    if args.target_username and args.target_password:
        target_auth = (args.target_username, args.target_password)

    inbox_auth = None
    if args.inbox_username and args.inbox_password:
        inbox_auth = (args.inbox_username, args.inbox_password)

    consumer = ldnlib.Consumer()

    inbox = consumer.discover(args.target, auth=target_auth)
    if inbox is not None:
        print("Found inbox: {}".format(inbox))
        for iri in consumer.notifications(inbox, auth=inbox_auth):
            print("")
            print("IRI: {}".format(iri))
            notification = consumer.notification(iri, auth=inbox_auth)
            print("Notification: {}".format(notification))
    else:
        print("Sorry, no inbox defined for the resource")
