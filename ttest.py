status = None

if not status:
    print("fsdsdfsf")


d = {}


d = {
    "version": 0,
    "accountId": "3a68c619-be54-4f3f-9843-550df646d149",
    "bot": "225596-sberavto-225596-TAf-2046143414",
    "channel": "sber_nlp2",
    "scenarioRevision": 76,
    "userId": "1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=-draft",
    "user": {
        "id": "1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=-draft",
        "firstName": "Sber user",
        "clientProfile": {
            "aggregated_data": """{args.channel=COMPANION_B2C, args.application_id=7aa5ae84-c668-4e24-94d8-e35cf053e7a1, args.project_name=c06f2c98-a899-44d7-8944-0d6e13108e99, args.message_id=1321647340, args.sub=1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=, args.project_id=12f20e40-efc6-4ff5-9179-f5c51f7197b3, args.user_id=2FB5249C-E0D4-408B-89C3-7EBE85C65A3C, args.app_version_id=af6d2a8e-39ba-46a6-a589-5e9db1194b85, args.surface=COMPANION, request_id=59eedc09-51a7-41d3-bdc7-a2d8ef20106e, args.message_name=MESSAGE_TO_SKILL
            }""",
            "userId": "2FB5249C-E0D4-408B-89C3-7EBE85C65A3C",
            "sub": "1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=",
            "userChannel": "COMPANION_B2C"
        }
    },
    "sessionId": "sdfsdfdsf",
    "questionId": "59eedc09-51a7-41d3-bdc7-a2d8ef20106e",
    "request": {
        "type": "QUERY",
        "query": "хочу бмв икс т** в мо**** д** ты**** пят********* года",
        "requestData": {
            "messageId": 1321647340,
            "sessionId": "b1456dc1-74a1-37d7-bc9f-1982dfc1b8aa",
            "messageName": "MESSAGE_TO_SKILL",
            "payload": {
                "intent": "sberauto_main",
                "original_intent": "video",
                "intent_meta": {},
                "message": {
                    "original_text": "хочу бмв икс т** в мо**** д** ты**** пят********* года",
                    "normalized_text": "хотеть бмв икс NUM_TOKEN в GEO_TOKEN TIME_DATE_TOKEN .",
                    "tokenized_elements_list": [
                        {
                            "text": "хочу",
                            "raw_text": "хочу",
                            "grammem_info": {
                                "aspect": "impf",
                                "mood": "ind",
                                "number": "sing",
                                "person": "1",
                                "tense": "notpast",
                                "transitivity": "tran",
                                "verbform": "fin",
                                "voice": "act",
                                "raw_gram_info": "aspect=impf|mood=ind|number=sing|person=1|tense=notpast|transitivity=tran|verbform=fin|voice=act",
                                "part_of_speech": "VERB"
                            },
                            "lemma": "хотеть",
                            "is_stop_word": False,
                            "list_of_dependents": [
                                3
                            ],
                            "dependency_type": "root",
                            "head": 0
                        },
                        {
                            "text": "бмв",
                            "raw_text": "бмв",
                            "grammem_info": {
                                "raw_gram_info": "",
                                "part_of_speech": "ADP"
                            },
                            "lemma": "бмв",
                            "is_stop_word": False,
                            "list_of_dependents": [],
                            "dependency_type": "case",
                            "head": 3
                        },
                        {
                            "text": "икс",
                            "raw_text": "икс",
                            "grammem_info": {
                                "animacy": "inan",
                                "case": "acc",
                                "gender": "masc",
                                "number": "sing",
                                "raw_gram_info": "animacy=inan|case=acc|gender=masc|number=sing",
                                "part_of_speech": "NOUN"
                            },
                            "lemma": "икс",
                            "is_stop_word": False,
                            "list_of_dependents": [
                                2,
                                4,
                                6
                            ],
                            "dependency_type": "obl",
                            "head": 1
                        },
                        {
                            "text": "3",
                            "raw_text": "3",
                            "lemma": "3",
                            "original_text": "т**",
                            "token_type": "NUM_TOKEN",
                            "token_value": {
                                "value": 3,
                                "adjectival_number": False
                            },
                            "list_of_token_types_data": [
                                {
                                    "token_type": "NUM_TOKEN",
                                    "token_value": {
                                        "value": 3,
                                        "adjectival_number": False
                                    }
                                }
                            ],
                            "grammem_info": {
                                "numform": "digit",
                                "raw_gram_info": "numform=digit",
                                "part_of_speech": "NUM"
                            },
                            "is_stop_word": False,
                            "list_of_dependents": [],
                            "dependency_type": "nummod",
                            "head": 3
                        },
                        {
                            "text": "в",
                            "raw_text": "в",
                            "grammem_info": {
                                "raw_gram_info": "",
                                "part_of_speech": "ADP"
                            },
                            "lemma": "в",
                            "is_stop_word": False,
                            "list_of_dependents": [],
                            "dependency_type": "case",
                            "head": 6
                        },
                        {
                            "text": "мо****",
                            "raw_text": "мо****",
                            "grammem_info": {
                                "animacy": "inan",
                                "case": "loc",
                                "gender": "fem",
                                "number": "sing",
                                "raw_gram_info": "animacy=inan|case=loc|gender=fem|number=sing",
                                "part_of_speech": "NOUN"
                            },
                            "lemma": "мо****",
                            "is_stop_word": False,
                            "list_of_dependents": [
                                5,
                                8
                            ],
                            "dependency_type": "nmod",
                            "head": 3,
                            "composite_token_type": "GEO_TOKEN",
                            "composite_token_length": 1,
                            "is_beginning_of_composite": True,
                            "composite_token_value": {
                                "value": "Мо****",
                                "locality_type": "CITY",
                                "latitude": 55.75222,
                                "longitude": 37.61556,
                                "capital": None,
                                "locative_value": {
                                    "CITY": "в Мо****"
                                },
                                "timezone": [
                                    [
                                        None,
                                        3.0
                                    ]
                                ],
                                "currency": [
                                    "RUB",
                                    "российский рубль"
                                ],
                                "country": "Ро****",
                                "country_hidden": False
                            }
                        },
                        {
                            "text": "2015",
                            "raw_text": "2015",
                            "lemma": "2015",
                            "original_text": "д** ты**** пят*********",
                            "token_type": "NUM_TOKEN",
                            "token_value": {
                                "value": 2015,
                                "adjectival_number": True
                            },
                            "list_of_token_types_data": [
                                {
                                    "token_type": "NUM_TOKEN",
                                    "token_value": {
                                        "value": 2015,
                                        "adjectival_number": True
                                    }
                                }
                            ],
                            "grammem_info": {
                                "numform": "digit",
                                "raw_gram_info": "numform=digit",
                                "part_of_speech": "NUM"
                            },
                            "is_stop_word": False,
                            "list_of_dependents": [],
                            "dependency_type": "nummod",
                            "head": 8,
                            "is_beginning_of_composite": True,
                            "composite_token_type": "TIME_DATE_TOKEN",
                            "composite_token_length": 2,
                            "composite_token_value": {
                                "year": 2015
                            }
                        },
                        {
                            "text": "года",
                            "raw_text": "года",
                            "grammem_info": {
                                "animacy": "inan",
                                "case": "gen",
                                "gender": "masc",
                                "number": "sing",
                                "raw_gram_info": "animacy=inan|case=gen|gender=masc|number=sing",
                                "part_of_speech": "NOUN"
                            },
                            "lemma": "год",
                            "is_stop_word": False,
                            "list_of_dependents": [
                                7
                            ],
                            "dependency_type": "nmod",
                            "head": 6,
                            "is_beginning_of_composite": False,
                            "composite_token_type": "TIME_DATE_TOKEN",
                            "composite_token_length": 2,
                            "composite_token_value": {
                                "year": 2015
                            }
                        },
                        {
                            "raw_text": ".",
                            "text": ".",
                            "lemma": ".",
                            "token_type": "SENTENCE_ENDPOINT_TOKEN",
                            "token_value": {
                                "value": "."
                            },
                            "list_of_token_types_data": [
                                {
                                    "token_type": "SENTENCE_ENDPOINT_TOKEN",
                                    "token_value": {
                                        "value": "."
                                    }
                                }
                            ]
                        }
                    ],
                    "entities": {
                        "NUM_TOKEN": [
                            {
                                "value": 3,
                                "adjectival_number": False
                            },
                            {
                                "value": 2015,
                                "adjectival_number": True
                            }
                        ],
                        "GEO_TOKEN": [
                            {
                                "value": "Мо****",
                                "locality_type": "CITY",
                                "latitude": 55.75222,
                                "longitude": 37.61556,
                                "capital": None,
                                "locative_value": {
                                    "CITY": "в Мо****"
                                },
                                "timezone": [
                                    [
                                        None,
                                        3.0
                                    ]
                                ],
                                "currency": [
                                    "RUB",
                                    "российский рубль"
                                ],
                                "country": "Ро****",
                                "country_hidden": False
                            }
                        ],
                        "TIME_DATE_TOKEN": [
                            {
                                "year": 2015
                            }
                        ]
                    },
                    "original_message_name": "VOICE_FROM_USER",
                    "human_normalized_text": "хотеть бмв икс 3 в мо**** 2015 год",
                    "asr_normalized_message": "Хочу бмв икс 3 в Мо**** 2015 года",
                    "human_normalized_text_with_anaphora": "хотеть бмв икс 3 в мо**** 2015 год"
                },
                "annotations": {
                    "censor_data": {
                        "classes": [
                            "politicians",
                            "obscene",
                            "model_response"
                        ],
                        "probas": [
                            0,
                            0,
                            1.5441773939528503E-6
                        ]
                    },
                    "text_sentiment": {
                        "classes": [
                            "negative",
                            "positive",
                            "neutral"
                        ],
                        "probas": [
                            0.002003005240112543,
                            0.008209338411688805,
                            0.9897876977920532
                        ]
                    },
                    "asr_sentiment": {
                        "classes": [
                            "positive",
                            "neutral",
                            "negative"
                        ],
                        "probas": [
                            0.015313976,
                            0.69002813,
                            0.2946578
                        ]
                    },
                    "ner_prediction": [
                        {
                            "raw_text": "хочу",
                            "lemma": "хотеть",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "O",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.99999726",
                                "main": "0.9994836",
                                "music": "0.99987817",
                                "odqa": "0.99997425",
                                "video": "0.999933"
                            }
                        },
                        {
                            "raw_text": "бмв",
                            "lemma": "бмв",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "B-ORG",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.58220047",
                                "main": "0.35833514",
                                "music": "0.95969045",
                                "odqa": "0.95633465",
                                "video": "0.8855663"
                            }
                        },
                        {
                            "raw_text": "икс",
                            "lemma": "икс",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "I-ORG",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.3918011",
                                "main": "0.9702003",
                                "music": "0.99877733",
                                "odqa": "0.95815533",
                                "video": "0.9829081"
                            }
                        },
                        {
                            "raw_text": "3",
                            "lemma": "3",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "I-ORG",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.023125948",
                                "main": "0.9912204",
                                "music": "0.9966793",
                                "odqa": "0.8536692",
                                "video": "0.91134113"
                            }
                        },
                        {
                            "raw_text": "в",
                            "lemma": "в",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "O",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.84274787",
                                "main": "0.95678425",
                                "music": "0.99996996",
                                "odqa": "0.99998486",
                                "video": "0.99651104"
                            }
                        },
                        {
                            "raw_text": "мо****",
                            "lemma": "мо****",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "B-LOC",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.9923584",
                                "main": "0.9885886",
                                "music": "0.99645895",
                                "odqa": "0.42336488",
                                "video": "0.99075574"
                            }
                        },
                        {
                            "raw_text": "2015",
                            "lemma": "2015",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "O",
                                "music": "O",
                                "odqa": "O",
                                "video": "B-YEAR"
                            },
                            "ner_label_probas": {
                                "food": "0.9991941",
                                "main": "0.99981433",
                                "music": "0.82854366",
                                "odqa": "0.8985298",
                                "video": "0.99837214"
                            }
                        },
                        {
                            "raw_text": "года",
                            "lemma": "год",
                            "normalized_token": None,
                            "ner_labels": {
                                "food": "O",
                                "main": "O",
                                "music": "O",
                                "odqa": "O",
                                "video": "O"
                            },
                            "ner_label_probas": {
                                "food": "0.9805228",
                                "main": "0.9999511",
                                "music": "0.9986713",
                                "odqa": "0.9999988",
                                "video": "0.9895419"
                            }
                        }
                    ],
                    "normalized_entities": {
                        "main": {}
                    }
                },
                "selected_item": {},
                "new_session": False,
                "strategies": {
                    "last_call": None
                },
                "character": {
                    "id": "sber",
                    "name": "Сбер",
                    "gender": "male",
                    "appeal": "official"
                },
                "asr": {
                    "hypotheses": [
                        {
                            "words": "хочу бмв икс т** в мо**** д** ты**** пят********* года",
                            "normalizedText": "Хочу бмв икс 3 в Мо**** 2015 года",
                            "extendedWords": [
                                {
                                    "tokenType": 1,
                                    "token": "хочу"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "бмв"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "икс"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "т**"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "в"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "мо****"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "д**"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "ты****"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "пят*********"
                                },
                                {
                                    "tokenType": 1,
                                    "token": "года"
                                }
                            ]
                        },
                        {
                            "words": "хочу bmw x т** в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу bmw x т** в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу бмв x т** в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу бмв x т** в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу bmw икс т** в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу bmw икс т** в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу bmw x three в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу bmw x three в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу бмв икс three в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу бмв икс three в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу бмв xx т** в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу бмв xx т** в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу бмв икс tree в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу бмв икс tree в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу бмв икс трим в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу бмв икс трим в мо**** д** ты**** пят********* года"
                        },
                        {
                            "words": "хочу bmw x tre в мо**** д** ты**** пят********* года",
                            "normalizedText": "хочу bmw x tre в мо**** д** ты**** пят********* года"
                        }
                    ],
                    "sentiment": {
                        "classes": [
                            "positive",
                            "neutral",
                            "negative"
                        ],
                        "probas": [
                            0.015313976,
                            0.69002813,
                            0.2946578
                        ]
                    }
                },
                "applicationId": "7aa5ae84-c668-4e24-94d8-e35cf053e7a1",
                "appversionId": "af6d2a8e-39ba-46a6-a589-5e9db1194b85",
                "projectName": "c06f2c98-a899-44d7-8944-0d6e13108e99",
                "device": {
                    "platformType": "IOS",
                    "platformVersion": "15.0",
                    "surface": "COMPANION",
                    "surfaceVersion": "21.8.2001",
                    "features": {
                        "appTypes": [
                            "DIALOG",
                            "WEB_APP",
                            "CHAT_APP"
                        ],
                        "clientFlags": {
                            "messengerEnabled": False,
                            "salute20Enabled": False
                        }
                    },
                    "capabilities": {
                        "screen": {
                            "available": True,
                            "height": 1792,
                            "scale_factor": 2,
                            "width": 828
                        }
                    },
                    "deviceId": "E7BD6F9B-B5C4-468C-929E-A5D83C1330FE",
                    "deviceManufacturer": "Apple",
                    "deviceModel": "iPhone12,1",
                    "additionalInfo": {
                        "host_app_id": "ru.sberdevices.companion",
                        "sdk_version": "21.8.2001"
                    }
                },
                "app_info": {
                    "projectId": "12f20e40-efc6-4ff5-9179-f5c51f7197b3",
                    "applicationId": "7aa5ae84-c668-4e24-94d8-e35cf053e7a1",
                    "appversionId": "af6d2a8e-39ba-46a6-a589-5e9db1194b85",
                    "systemName": None,
                    "frontendEndpoint": None,
                    "frontendType": "DIALOG",
                    "ageLimit": 0
                },
                "meta": {
                    "current_app": {},
                    "time": {
                        "timezone_offset_sec": 10800,
                        "timestamp": 1632738694696,
                        "timezone_id": "Europe/Moscow"
                    },
                    "location": {},
                    "features": {
                        "screen": {
                            "enabled": True
                        },
                        "int_login": {
                            "enabled": True
                        },
                        "demo_mode": {
                            "enabled": False
                        }
                    },
                    "background_apps": [],
                    "child_mode": False
                },
                "client_profile": {
                    "aggregated_data": {}
                }
            },
            "uuid": {
                "userId": "2FB5249C-E0D4-408B-89C3-7EBE85C65A3C",
                "sub": "1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=",
                "userChannel": "COMPANION_B2C"
            }
        },
        "data": {}
    },
    "nlpInfo": {
        "fromState": "/Car",
        "nlpClass": "/Car",
        "rule": "*",
        "ruleType": "pattern",
        "confidence": -0.010177777777777742
    },
    "response": {
        "responseData": {
            "nlpClass": "/Car",
            "confidence": -0.010177777777777742,
            "replies": [
                {
                    "type": "raw",
                    "body": {
                        "pronounceText": "На экране показываю, какие варианты удалось найти. А посмотреть каждый из них можно в Сбер А'вто",
                        "emotion": None,
                        "items": [
                            {
                                "card": {
                                    "type": "list_card",
                                    "cells": [
                                        {
                                            "type": "image_cell_view",
                                            "content": {
                                                "url": "https://content.sberdevices.ru/smartmarket-smide-prod/225583/225582/yd9ak7aehfSkuOVF.png",
                                                "width": "small",
                                                "aspect_ratio": 1
                                            }
                                        },
                                        {
                                            "type": "text_cell_view",
                                            "content": {
                                                "text": "По запросу",
                                                "typeface": "body1",
                                                "text_color": "secondary",
                                                "max_lines": 0
                                            },
                                            "paddings": {
                                                "left": "8x",
                                                "top": "10x",
                                                "right": "8x"
                                            }
                                        },
                                        {
                                            "type": "text_cell_view",
                                            "content": {
                                                "text": "«BMW X3 Мо**** 2015 года»",
                                                "typeface": "body1",
                                                "text_color": "default",
                                                "max_lines": 0
                                            },
                                            "paddings": {
                                                "left": "8x",
                                                "top": "2x",
                                                "right": "8x"
                                            }
                                        },
                                        {
                                            "type": "text_cell_view",
                                            "content": {
                                                "text": "3 предложения",
                                                "typeface": "body1",
                                                "text_color": "default",
                                                "max_lines": 0
                                            },
                                            "paddings": {
                                                "left": "8x",
                                                "top": "2x",
                                                "right": "8x"
                                            }
                                        },
                                        {
                                            "type": "text_cell_view",
                                            "content": {
                                                "text": "от 1.9 м** до 2.4 м** ₽,",
                                                "typeface": "body1",
                                                "text_color": "default",
                                                "max_lines": 0
                                            },
                                            "paddings": {
                                                "left": "8x",
                                                "top": "10x",
                                                "right": "8x"
                                            }
                                        },
                                        {
                                            "type": "text_cell_view",
                                            "content": {
                                                "text": "средняя цена — 2.3 м** ₽",
                                                "typeface": "body1",
                                                "text_color": "secondary",
                                                "max_lines": 0
                                            },
                                            "paddings": {
                                                "left": "8x",
                                                "top": "2x",
                                                "right": "8x"
                                            }
                                        },
                                        {
                                            "type": "button_cell_view",
                                            "content": {
                                                "text": "Посмотреть в СберАвто",
                                                "typeface": "button1",
                                                "style": "default",
                                                "type": "accept",
                                                "actions": [
                                                    {
                                                        "type": "deep_link",
                                                        "text": "Посмотреть в СберАвто",
                                                        "deep_link": "https://sberauto.onelink.me/RBOE/applisting?year_to=2015&year_from=2015&city_id=%5B1%5D&catalog=%5B%7B%22brand_id%22%3A48%2C%22model_id%22%3A%5B588%5D%7D%5D"
                                                    }
                                                ],
                                                "margins": {
                                                    "left": "10x",
                                                    "top": "5x",
                                                    "right": "10x",
                                                    "bottom": "5x"
                                                }
                                            },
                                            "paddings": {
                                                "left": "6x",
                                                "top": "12x",
                                                "right": "6x",
                                                "bottom": "8x"
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "messageName": "ANSWER_TO_USER"
                }
            ],
            "facebookMenuTitle": "Menu",
            "facebookPlainButtons": True,
            "sessionId": "1QMkO51SGavO0qmdynJIMb5TW0Yt6moxl8yY0QvR0Fqx2JbDyI+RqOTRnuTgUhdUnOP7vtkAUnImVX2AhJGfHYKRiXJlPuwyOeNolA7wjKYiOZlDM6uI6ENVPLiM6ow3nM7VHQQb3n1vILcVIS2OFwbZw8/jODOC5TFmXuIoX74=-draft.8f8f115b-5067-4d9d-b212-31fefe6b3047"
        }
    },
    "httpRequests": [],
    "formattedDate": "2021-09-27T10:31:39Z",
    "timestamp": 1632738699989,
    "processingTime": 2671,
    "start": 1632738699849,
    "end": 0,
    "logType": "LOG_REQUEST",
    "time": 1632738699989,
    "botId": "225596-sberavto-225596-TAf-2046143414",
    "channelType": "sber_nlp2",
    "query": "хочу бмв икс т** в мо**** д** ты**** пят********* года"
}

tokenized_elements_list = d.get("request", {}).get("requestData", {}).get("payload", {}).get("message", {}).get("tokenized_elements_list", [])

dirty_text = " ".join([x["text"] for x in tokenized_elements_list])

print(dirty_text)



