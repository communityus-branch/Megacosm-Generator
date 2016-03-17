#

self.redis.lpush('npc_race', 'goblin')

SET goblin_details     {"name": "Goblin",     "size": "small",   "description": "their small stature and conniving"}

self.redis.lpush('goblin_covering', 'skin')

SET goblin_subrace_chance 30
# Note that descriptions aren\'t heavily used right now anyways.
self.redis.lpush('goblin_subrace', 'night')
self.redis.lpush('goblin_subrace', 'fire')
self.redis.lpush('goblin_subrace', 'dust')
self.redis.lpush('goblin_subrace', 'hill')

self.redis.hset('goblin_subrace_description', 'night', '{"subrace": "Night Goblin",      "description": "" }')
self.redis.hset('goblin_subrace_description', 'fire', '{"subrace": "Fire Goblin",       "description": "" }')
self.redis.hset('goblin_subrace_description', 'dust', '{"subrace": "Dust Goblin",       "description": "" }')
self.redis.hset('goblin_subrace_description', 'hill', '{"subrace": "Hill Goblin",       "description": "" }')
self.redis.hset('goblin_subrace_description', 'tooth', '{"subrace": "Tooth Goblin",       "description": "" }')


self.redis.lpush('goblinname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
self.redis.lpush('goblinname_shortname_template', '{{params.first_pre}}{{params.first_root}}')
self.redis.lpush('goblinname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')

set goblinname_first_pre_chance 100
set goblinname_first_root_chance 100
set goblinname_last_pre_chance 100
set goblinname_last_root_chance 100


self.redis.lpush('goblinname_first_pre', 'Br')
self.redis.lpush('goblinname_first_pre', 'Dzu')
self.redis.lpush('goblinname_first_pre', 'Gkut')
self.redis.lpush('goblinname_first_pre', 'K')
self.redis.lpush('goblinname_first_pre', 'K')
self.redis.lpush('goblinname_first_pre', 'Kz')
self.redis.lpush('goblinname_first_pre', 'M')
self.redis.lpush('goblinname_first_pre', 'M')
self.redis.lpush('goblinname_first_pre', 'Nar')
self.redis.lpush('goblinname_first_pre', 'Nb')
self.redis.lpush('goblinname_first_pre', 'Rb')
self.redis.lpush('goblinname_first_pre', 'Rug')
self.redis.lpush('goblinname_first_pre', 'Rx')
self.redis.lpush('goblinname_first_pre', 'Tb')
self.redis.lpush('goblinname_first_pre', 'Tg')
self.redis.lpush('goblinname_first_pre', 'Tm')
self.redis.lpush('goblinname_first_pre', 'Tr')
self.redis.lpush('goblinname_first_pre', 'Tud')
self.redis.lpush('goblinname_first_pre', 'Xod')
self.redis.lpush('goblinname_first_pre', 'Xr')
self.redis.lpush('goblinname_first_pre', 'Xt')
self.redis.lpush('goblinname_first_pre', 'Xu')
self.redis.lpush('goblinname_first_pre', 'Z')
self.redis.lpush('goblinname_first_root', 'adr')
self.redis.lpush('goblinname_first_root', 'bok')
self.redis.lpush('goblinname_first_root', 'eb')
self.redis.lpush('goblinname_first_root', 'egd')
self.redis.lpush('goblinname_first_root', 'emt')
self.redis.lpush('goblinname_first_root', 'erm')
self.redis.lpush('goblinname_first_root', 'et')
self.redis.lpush('goblinname_first_root', 'exn')
self.redis.lpush('goblinname_first_root', 'ezn')
self.redis.lpush('goblinname_first_root', 'kasr')
self.redis.lpush('goblinname_first_root', 'ods')
self.redis.lpush('goblinname_first_root', 'og')
self.redis.lpush('goblinname_first_root', 'ok')
self.redis.lpush('goblinname_first_root', 'omd')
self.redis.lpush('goblinname_first_root', 'omn')
self.redis.lpush('goblinname_first_root', 'or')
self.redis.lpush('goblinname_first_root', 'ot')
self.redis.lpush('goblinname_first_root', 'oten')
self.redis.lpush('goblinname_first_root', 'ub')
self.redis.lpush('goblinname_first_root', 'uk')
self.redis.lpush('goblinname_first_root', 'un')
self.redis.lpush('goblinname_first_root', 'unk')
self.redis.lpush('goblinname_first_root', 'urm')
self.redis.lpush('goblinname_first_root', 'us')
self.redis.lpush('goblinname_first_root', 'zar')

self.redis.lpush('goblinname_last_pre', 'Big')
self.redis.lpush('goblinname_last_pre', 'Blade')
self.redis.lpush('goblinname_last_pre', 'Brain')
self.redis.lpush('goblinname_last_pre', 'Cleaver')
self.redis.lpush('goblinname_last_pre', 'Damn')
self.redis.lpush('goblinname_last_pre', 'Dark')
self.redis.lpush('goblinname_last_pre', 'Dread')
self.redis.lpush('goblinname_last_pre', 'Evil')
self.redis.lpush('goblinname_last_pre', 'Foul')
self.redis.lpush('goblinname_last_pre', 'Ghostt')
self.redis.lpush('goblinname_last_pre', 'Giant')
self.redis.lpush('goblinname_last_pre', 'Great')
self.redis.lpush('goblinname_last_pre', 'Great')
self.redis.lpush('goblinname_last_pre', 'Iron')
self.redis.lpush('goblinname_last_pre', 'Laugh')
self.redis.lpush('goblinname_last_pre', 'Metal')
self.redis.lpush('goblinname_last_pre', 'Metal')
self.redis.lpush('goblinname_last_pre', 'Night')
self.redis.lpush('goblinname_last_pre', 'Ogre')
self.redis.lpush('goblinname_last_pre', 'Ooze')
self.redis.lpush('goblinname_last_pre', 'Rant')
self.redis.lpush('goblinname_last_pre', 'Rock')
self.redis.lpush('goblinname_last_pre', 'Worm')

self.redis.lpush('goblinname_last_root', 'basher')
self.redis.lpush('goblinname_last_root', 'beast')
self.redis.lpush('goblinname_last_root', 'bone')
self.redis.lpush('goblinname_last_root', 'cutter')
self.redis.lpush('goblinname_last_root', 'damn')
self.redis.lpush('goblinname_last_root', 'death')
self.redis.lpush('goblinname_last_root', 'doom')
self.redis.lpush('goblinname_last_root', 'fury')
self.redis.lpush('goblinname_last_root', 'gloom')
self.redis.lpush('goblinname_last_root', 'hand')
self.redis.lpush('goblinname_last_root', 'host')
self.redis.lpush('goblinname_last_root', 'howl')
self.redis.lpush('goblinname_last_root', 'kill')
self.redis.lpush('goblinname_last_root', 'maw')
self.redis.lpush('goblinname_last_root', 'mouth')
self.redis.lpush('goblinname_last_root', 'murder')
self.redis.lpush('goblinname_last_root', 'render')
self.redis.lpush('goblinname_last_root', 'rot')
self.redis.lpush('goblinname_last_root', 'shadow')
self.redis.lpush('goblinname_last_root', 'shredder')
self.redis.lpush('goblinname_last_root', 'slay')
self.redis.lpush('goblinname_last_root', 'stomach')
self.redis.lpush('goblinname_last_root', 'wiser')

