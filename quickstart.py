from instapy import InstaPy

session = InstaPy(username='ombajans', password='karatas35.')

session.login()

session.set_do_follow(enabled=True, percentage=100, times=1)
session.like_by_locations(['235120292/manavgat-antalya/', '1890895921171803/manavgat-irmak-kenar-yuruyus-yolu/', '148004049297143/manavgat-turk-kahvesi/', '686798411473021/novamall/', '630484290446062/bayramefendi-osmanl-kahvecisi/', '288739318/pepper-lounge/', '296220761/cumhuriyet-meydan-manavgat/', '250739372055182/mod-house-manavgat/'], amount=120, media=None)

session.follow_user_followers(['birsevdadirmanavgat'], amount=120, sleep_delay=30, randomize=True, interact=False)
session.unfollow_users(amount=1080, sleep_delay=10)

session.end()