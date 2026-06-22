# content.py

# Each stream = a key. Each stream has "boxes" (categories), 
# each box has a list of lessons.
# content.py (sirf "student" key ka updated version - GovT/Tech wale neeche same rahenge)

CONTENT = {
    "student": {
        "display_name": "Student (School & College)",
        "boxes": [
            {
                "id": "chatgpt",
                "title": "ChatGPT",
                "icon": "💬",
                "description": "Your everyday AI assistant for explanations, study help and writing",
                "lessons": [
                    {
                        "id": "chatgpt-getting-started",
                        "title": "What is ChatGPT and how to get started",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Before using ChatGPT for studying, you need to understand what it actually is and set up your free account properly.",
                        "steps": [
                            {
                                "title": "Go to chat.openai.com",
                                "text": "This is the official ChatGPT website. Avoid random apps claiming to be 'ChatGPT' — use the official site or app only."
                            },
                            {
                                "title": "Create a free account",
                                "text": "Sign up using your email or Google account. The free version (GPT-5.1) is enough for almost all student use."
                            },
                            {
                                "title": "Type your first message",
                                "text": "Try something simple first to understand how it replies.",
                                "prompt": "Explain photosynthesis to me like I'm in 8th grade, in under 100 words."
                            },
                            {
                                "title": "Notice it remembers the conversation",
                                "text": "Unlike Google search, you can ask a follow-up question like 'explain that again but simpler' and it understands the context."
                            }
                        ],
                        "tip": "Everything you type can be edited — hover over your old message and click the pencil icon to fix a typo instead of retyping everything."
                    },
                    {
                        "id": "chatgpt-study-buddy",
                        "title": "Turn ChatGPT into your personal study buddy",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Most students just ask ChatGPT random questions. This sets it up to actually quiz you and track weak topics.",
                        "steps": [
                            {
                                "title": "Open a new chat",
                                "text": "Click 'New chat' in the sidebar."
                            },
                            {
                                "title": "Paste this setup prompt first",
                                "text": "This tells ChatGPT exactly how to behave for the rest of the conversation.",
                                "prompt": "Act as my personal study tutor for [SUBJECT NAME]. Ask me one question at a time. If I get it wrong, explain the correct answer simply before moving to the next question. Keep track of which topics I struggle with and remind me at the end."
                            },
                            {
                                "title": "Replace [SUBJECT NAME]",
                                "text": "Type your actual subject, like 'Class 10 Science - Light chapter' instead of the bracket."
                            },
                            {
                                "title": "Answer honestly",
                                "text": "Don't just say 'correct' to skip ahead — the more honest you are, the better it tailors questions to your weak spots."
                            }
                        ],
                        "tip": "At the end of a session, ask: 'Summarize the 3 topics I struggled with most.' Save that list and revise it before exams."
                    },
                    {
                        "id": "chatgpt-essay-feedback",
                        "title": "Get real feedback on your essays (without AI writing it for you)",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Using AI to write your essay can get you in trouble and you won't learn. This uses AI as a strict teacher instead.",
                        "steps": [
                            {
                                "title": "Write your essay yourself first",
                                "text": "AI should review, not create. Write your full draft normally."
                            },
                            {
                                "title": "Paste your essay with this instruction before it",
                                "text": "This forces feedback instead of a rewrite.",
                                "prompt": "You are a strict but encouraging English teacher. Do NOT rewrite my essay. Instead, point out: 1) grammar mistakes with the fix, 2) weak sentences and why, 3) one thing I did well. Here is my essay:"
                            },
                            {
                                "title": "Paste your essay text right after",
                                "text": "Just type or paste your essay directly below the instruction in the same message."
                            },
                            {
                                "title": "Fix it yourself",
                                "text": "Go through the feedback and rewrite the weak parts in your own words — this is the part that actually improves your writing."
                            }
                        ],
                        "tip": "Ask it to rate your essay 1-10 and explain exactly what's stopping it from being a 10."
                    }
                ]
            },
            {
                "id": "gemini",
                "title": "Google Gemini",
                "icon": "✨",
                "description": "Best if you already use Gmail, Docs and Drive — works inside Google apps",
                "lessons": [
                    {
                        "id": "gemini-getting-started",
                        "title": "Getting started with Google Gemini",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Gemini works right inside Gmail, Docs and Drive if you already use a Google account — no separate signup needed.",
                        "steps": [
                            {
                                "title": "Go to gemini.google.com",
                                "text": "Sign in with the same Google account you use for Gmail/Drive."
                            },
                            {
                                "title": "Check if you have a free student plan",
                                "text": "If you have a college .edu-style email, look for a student offer — it unlocks the Pro model and NotebookLM Plus for free for a year in many regions."
                            },
                            {
                                "title": "Try your first question",
                                "text": "Ask something and notice it can also search the web for current information.",
                                "prompt": "What are 3 effective ways to revise for exams using active recall?"
                            },
                            {
                                "title": "Try it inside Google Docs too",
                                "text": "Open a Google Doc, look for the Gemini icon in the top right, and ask it to help draft or improve your writing directly there."
                            }
                        ],
                        "tip": "If you're stuck between ChatGPT and Gemini, use Gemini when your work already lives in Google Docs/Drive — it saves you copy-pasting back and forth."
                    },
                    {
                        "id": "gemini-gems",
                        "title": "How to build your own Gem in Google Gemini",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "A Gem is your own mini-version of Gemini trained for one job — like a homework helper.",
                        "steps": [
                            {
                                "title": "Open Gemini and find Gems",
                                "text": "Go to gemini.google.com, look at the left sidebar, click 'Gem manager.'"
                            },
                            {
                                "title": "Click 'New Gem'",
                                "text": "A blank box opens where you describe what your Gem should do."
                            },
                            {
                                "title": "Paste this exact instruction",
                                "text": "This is the 'brain' of your Gem.",
                                "prompt": "You are a friendly homework helper for a 10th grade student. Explain answers in simple steps. Never just give the final answer — always explain the why first. Keep replies under 150 words."
                            },
                            {
                                "title": "Name it and save",
                                "text": "Call it 'Homework helper,' click save — it now appears every time you open Gemini."
                            }
                        ],
                        "tip": "Ask your new Gem to explain a tricky math question, then compare it to asking plain Gemini."
                    },
                    {
                        "id": "gemini-research-helper",
                        "title": "Research any college project topic properly with Gemini",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "Helps you build a project/assignment structure instead of just copying random internet content.",
                        "steps": [
                            {
                                "title": "Open Gemini",
                                "text": "Go to gemini.google.com."
                            },
                            {
                                "title": "Describe your project clearly",
                                "text": "The more specific you are, the better the structure you'll get.",
                                "prompt": "I have a college project on [YOUR TOPIC]. Give me: 1) a clear outline with sections, 2) 3 key questions my project should answer, 3) what kind of sources I should look for (without making them up)."
                            },
                            {
                                "title": "Replace [YOUR TOPIC]",
                                "text": "Type your actual project subject in place of the bracket."
                            },
                            {
                                "title": "Verify sources yourself",
                                "text": "Gemini can suggest source types, but always verify facts/sources yourself before submitting — never copy AI-written content directly into your project."
                            }
                        ],
                        "tip": "Ask it to also generate 5 viva/exam questions your teacher might ask about this topic, so you're prepared to defend your project."
                    }
                ]
            },
            {
                "id": "claude",
                "title": "Claude",
                "icon": "🧠",
                "description": "Best for handling long PDFs and giving honest, detailed feedback",
                "lessons": [
                    {
                        "id": "claude-getting-started",
                        "title": "Getting started with Claude",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Claude is especially good at reading long documents fully and giving careful, detailed answers rather than quick shallow ones.",
                        "steps": [
                            {
                                "title": "Go to claude.ai",
                                "text": "Sign up with your email or Google account — free plan included."
                            },
                            {
                                "title": "Start a new chat",
                                "text": "Click the '+' or 'New chat' button."
                            },
                            {
                                "title": "Try asking it to explain something in depth",
                                "text": "Claude tends to give more thorough, structured answers than quick one-liners.",
                                "prompt": "Explain the causes of World War 1 in a structured way with clear sections, suitable for a college history essay."
                            },
                            {
                                "title": "Notice the attach/paperclip icon",
                                "text": "This lets you upload PDFs, images, or documents directly — you'll use this a lot for textbook chapters."
                            }
                        ],
                        "tip": "Free plan has daily limits that reset — if it says you're out of messages, you can usually continue in a few hours."
                    },
                    {
                        "id": "claude-pdf-notes",
                        "title": "Turn any PDF textbook chapter into short notes using Claude",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Instead of reading a 20-page chapter, get clean, exam-ready notes in seconds.",
                        "steps": [
                            {
                                "title": "Open Claude",
                                "text": "Go to claude.ai and start a new chat."
                            },
                            {
                                "title": "Upload your PDF chapter",
                                "text": "Click the paperclip/attach icon near the message box and select your PDF file."
                            },
                            {
                                "title": "Type this exact instruction",
                                "text": "This controls exactly how the notes look.",
                                "prompt": "Summarize this chapter as exam-ready short notes. Use bullet points, bold the most important terms, and add a 5-question quiz at the end to test my understanding."
                            },
                            {
                                "title": "Test yourself with the quiz",
                                "text": "Don't just read the notes — actually try answering the quiz it generates before checking answers."
                            }
                        ],
                        "tip": "Works great the night before an exam — upload the whole chapter and ask for 'only the topics that are usually asked in exams.'"
                    },
                    {
                        "id": "claude-projects",
                        "title": "Use Claude Projects to organize all your subject notes in one place",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Instead of starting from zero every chat, Projects let you keep all your syllabus material in one space that Claude remembers throughout the conversation.",
                        "steps": [
                            {
                                "title": "Click 'Projects' in the left sidebar",
                                "text": "Then click 'Create project.'"
                            },
                            {
                                "title": "Name it after your subject",
                                "text": "Example: 'Class 12 Physics' or 'Semester 3 - DBMS'."
                            },
                            {
                                "title": "Upload your syllabus and key notes",
                                "text": "Add your syllabus PDF, important chapters, and any formula sheets into the project's knowledge area."
                            },
                            {
                                "title": "Start chatting inside the project",
                                "text": "Now every question you ask inside this project automatically considers your uploaded material — no need to re-upload each time."
                            }
                        ],
                        "tip": "Create one project per subject — keeps each subject's context clean instead of one messy mixed chat history."
                    }
                ]
            },
            {
                "id": "notebooklm",
                "title": "NotebookLM",
                "icon": "📓",
                "description": "Turns your own notes and lectures into an interactive study assistant",
                "lessons": [
                    {
                        "id": "notebooklm-getting-started",
                        "title": "What is NotebookLM and how it's different from ChatGPT",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "NotebookLM only answers based on documents YOU upload — it won't make things up from the open internet, which makes it more trustworthy for exam revision.",
                        "steps": [
                            {
                                "title": "Go to notebooklm.google.com",
                                "text": "Sign in with your Google account."
                            },
                            {
                                "title": "Click 'New notebook'",
                                "text": "This creates an empty workspace tied to your own sources."
                            },
                            {
                                "title": "Upload one document to test",
                                "text": "Try a single lecture PDF or your class notes first."
                            },
                            {
                                "title": "Ask a question about only that document",
                                "text": "Notice it gives you the answer WITH a clickable citation showing exactly which page it came from.",
                                "prompt": "What are the 3 most important points in this document?"
                            }
                        ],
                        "tip": "Because it only uses what you upload, it's safe for fact-heavy subjects like history or law where you can't risk made-up answers."
                    },
                    {
                        "id": "notebooklm-study-notebook",
                        "title": "Build your own AI study notebook from your class notes",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "Combine an entire subject's material into one notebook so you can ask questions across all your lectures at once, not just one document.",
                        "steps": [
                            {
                                "title": "Create a notebook per subject",
                                "text": "Name it clearly, like 'Organic Chemistry - Full Semester.'"
                            },
                            {
                                "title": "Upload everything for that subject",
                                "text": "Add all lecture slides, your handwritten notes (scanned/photographed), and the textbook PDF if you have it. NotebookLM can handle up to 50 sources per notebook."
                            },
                            {
                                "title": "Ask cross-document questions",
                                "text": "This is where it gets powerful — ask things that need information from multiple files at once.",
                                "prompt": "Compare how lecture 3 and lecture 7 both explain oxidation reactions. Are there any differences in how they're presented?"
                            },
                            {
                                "title": "Generate a study guide",
                                "text": "Click the 'Study guide' option in the notebook to auto-generate a structured revision document from everything you uploaded."
                            }
                        ],
                        "tip": "Upload your old exam papers too if you have them — ask it to identify which topics appear most frequently across past papers."
                    },
                    {
                        "id": "notebooklm-audio-overview",
                        "title": "Generate an audio overview (podcast) of your notes to revise on the go",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "NotebookLM can turn your uploaded notes into a podcast-style conversation you can listen to while traveling or doing chores.",
                        "steps": [
                            {
                                "title": "Open a notebook with your sources already uploaded",
                                "text": "This works on any notebook that already has documents in it."
                            },
                            {
                                "title": "Find 'Audio Overview' on the right panel",
                                "text": "Click 'Generate' next to it."
                            },
                            {
                                "title": "Wait a few minutes",
                                "text": "It creates a natural-sounding two-person discussion explaining your material, usually 5-15 minutes long."
                            },
                            {
                                "title": "Listen and pause to think",
                                "text": "Treat it like a real lecture — pause if something needs more thought, don't just let it play in the background unattended."
                            }
                        ],
                        "tip": "Great for auditory learners or for revising during a commute when you can't read a textbook — but it should add to reading, not fully replace it."
                    }
                ]
            },
            {
                "id": "perplexity",
                "title": "Perplexity",
                "icon": "🔎",
                "description": "Best for research — gives real sources and citations, not just answers",
                "lessons": [
                    {
                        "id": "perplexity-getting-started",
                        "title": "What is Perplexity and why it's better for research than ChatGPT",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Perplexity is built to search the live internet and show you exactly which sources its answer came from — closer to a smart search engine than a chatbot.",
                        "steps": [
                            {
                                "title": "Go to perplexity.ai",
                                "text": "Sign up free with email or Google."
                            },
                            {
                                "title": "Ask a question that needs current information",
                                "text": "Try something that needs up-to-date facts, not something ChatGPT might guess from old training data.",
                                "prompt": "What were the key findings of the most recent NCERT curriculum update?"
                            },
                            {
                                "title": "Look at the numbered sources",
                                "text": "Notice small numbers next to sentences — click them to see exactly which website the claim came from."
                            },
                            {
                                "title": "Click through to a source",
                                "text": "Always open at least one source for anything you plan to use in an actual assignment."
                            }
                        ],
                        "tip": "If a claim has no citation number next to it, treat it with more caution — verify it elsewhere before trusting it."
                    },
                    {
                        "id": "perplexity-research-citations",
                        "title": "Research any topic with real citations using Perplexity",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Use this for assignments where your teacher expects you to actually cite sources, not just submit AI-written paragraphs.",
                        "steps": [
                            {
                                "title": "Be specific about what you need",
                                "text": "Vague questions get vague sources.",
                                "prompt": "Find 5 credible sources discussing the economic impact of renewable energy adoption in India between 2023 and 2026. List the source name and one key stat from each."
                            },
                            {
                                "title": "Copy the source names, not just the answer",
                                "text": "You need the actual source list for your bibliography, not just Perplexity's summary."
                            },
                            {
                                "title": "Open each source and verify",
                                "text": "Quickly skim each linked article to confirm it actually says what Perplexity claims it says."
                            },
                            {
                                "title": "Write your assignment in your own words",
                                "text": "Use the sources as your research base, but write the actual content yourself."
                            }
                        ],
                        "tip": "Ask follow-up questions like 'are any of these sources biased or one-sided?' to practice critical thinking about your sources."
                    },
                    {
                        "id": "perplexity-academic-mode",
                        "title": "Use Perplexity's Academic mode for trustworthy sources",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "A special mode that searches academic papers and journals specifically, instead of general websites and blogs.",
                        "steps": [
                            {
                                "title": "Look for the search mode selector",
                                "text": "Near the search bar, find the option to switch search focus/mode."
                            },
                            {
                                "title": "Select 'Academic'",
                                "text": "This limits results to scholarly papers and journals instead of random blog posts."
                            },
                            {
                                "title": "Ask your research question",
                                "text": "Best for college-level assignments needing peer-reviewed backing.",
                                "prompt": "What does recent research say about the effectiveness of spaced repetition for long-term memory retention?"
                            },
                            {
                                "title": "Check publication dates",
                                "text": "Older papers aren't necessarily wrong, but note the year — fast-moving fields need recent sources."
                            }
                        ],
                        "tip": "Academic mode is slower than normal search — use it specifically for serious assignments and research papers, not quick daily questions."
                    }
                ]
            }
        ]
    },
    # content.py - replace the "govt_employee" and "tech_employee" sections with these

    "govt_employee": {
        "display_name": "Government Employee",
        "boxes": [
            {
                "id": "chatgpt",
                "title": "ChatGPT",
                "icon": "💬",
                "description": "Drafting letters, applications and general office writing",
                "lessons": [
                    {
                        "id": "chatgpt-getting-started",
                        "title": "What is ChatGPT and how to get started",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "A simple introduction before you start using ChatGPT for office work.",
                        "steps": [
                            {
                                "title": "Go to chat.openai.com",
                                "text": "Use only the official website to avoid fake lookalike apps."
                            },
                            {
                                "title": "Create a free account",
                                "text": "Sign up with your email — the free plan is enough for most office tasks."
                            },
                            {
                                "title": "Ask your first question",
                                "text": "Try something simple to see how it responds.",
                                "prompt": "Explain in simple terms what a Right to Information (RTI) request is and how it usually gets processed."
                            },
                            {
                                "title": "Notice it remembers context",
                                "text": "You can ask follow-up questions like 'now make that shorter' and it understands what 'that' refers to."
                            }
                        ],
                        "tip": "Never paste confidential government data, citizen personal information, or classified content into any external AI tool."
                    },
                    {
                        "id": "chatgpt-official-letter",
                        "title": "Draft a perfect official letter or application using ChatGPT",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Instead of struggling with formal language, let AI write the first draft in proper government/office tone — you just fill in the details.",
                        "steps": [
                            {
                                "title": "Open ChatGPT",
                                "text": "Go to chat.openai.com and start a new chat."
                            },
                            {
                                "title": "Use this exact prompt structure",
                                "text": "Replace the brackets with your actual details.",
                                "prompt": "Write a formal official letter in Indian government office format. Purpose: [e.g. requesting leave / transfer / complaint]. My designation: [your post]. Department: [your department]. Keep tone respectful, concise, and follow standard government letter format with subject line and proper closing."
                            },
                            {
                                "title": "Fill in your real details",
                                "text": "Replace every bracket with your actual purpose, designation, and department before sending."
                            },
                            {
                                "title": "Check before sending",
                                "text": "Always read the AI draft fully and correct any wrong facts — AI doesn't know your actual case details, only you do."
                            }
                        ],
                        "tip": "Ask it to also give you 2 alternate versions — one more formal, one shorter — so you can pick what fits your office's style."
                    },
                    {
                        "id": "chatgpt-meeting-minutes",
                        "title": "Turn rough meeting notes into clean Minutes of Meeting (MoM)",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Take messy handwritten or typed notes during a meeting, and convert them into a proper, shareable MoM document.",
                        "steps": [
                            {
                                "title": "Type out your rough notes",
                                "text": "Don't worry about grammar or order — just get all points down during/after the meeting."
                            },
                            {
                                "title": "Paste your notes with this instruction",
                                "text": "This converts messy points into a proper format.",
                                "prompt": "Convert these rough meeting notes into a formal Minutes of Meeting document with sections: Attendees, Key Discussion Points, Decisions Taken, Action Items (with responsible person if mentioned). Here are my notes:"
                            },
                            {
                                "title": "Paste your actual notes after",
                                "text": "Add your rough notes directly below the instruction in the same message."
                            },
                            {
                                "title": "Review and correct names/decisions",
                                "text": "AI can misread or rearrange details — always verify names, decisions, and action items before circulating."
                            }
                        ],
                        "tip": "Ask it to also list 'pending items from last meeting that weren't addressed' if you paste the previous MoM along with new notes."
                    }
                ]
            },
            {
                "id": "gemini",
                "title": "Google Gemini",
                "icon": "✨",
                "description": "Best if your office already uses Gmail, Docs and Drive",
                "lessons": [
                    {
                        "id": "gemini-getting-started",
                        "title": "Getting started with Google Gemini",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "If your office already uses Gmail and Google Drive, Gemini works directly inside those tools without any extra setup.",
                        "steps": [
                            {
                                "title": "Go to gemini.google.com",
                                "text": "Sign in with the same Google account you use for office email."
                            },
                            {
                                "title": "Try your first question",
                                "text": "Ask something work-related to see how it responds.",
                                "prompt": "Summarize the key responsibilities of a government office in handling public grievances, in 5 bullet points."
                            },
                            {
                                "title": "Try it inside Gmail",
                                "text": "Open Gmail, look for the Gemini icon when composing a reply — it can draft a reply to an email for you based on the thread."
                            },
                            {
                                "title": "Try it inside Google Docs",
                                "text": "Open a Google Doc, click the Gemini icon, and ask it to help draft or restructure a document directly there."
                            }
                        ],
                        "tip": "Always re-read any auto-drafted email reply fully before sending — never send an AI draft without checking it represents you correctly."
                    },
                    {
                        "id": "gemini-report-summary",
                        "title": "Summarize long government reports or circulars instantly with Gemini",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Long circulars and policy documents take forever to read fully. Get the key points in seconds.",
                        "steps": [
                            {
                                "title": "Open Gemini",
                                "text": "Go to gemini.google.com."
                            },
                            {
                                "title": "Upload or paste the document",
                                "text": "Click the attach icon to upload a PDF, or copy-paste the circular text directly into the chat."
                            },
                            {
                                "title": "Type this instruction",
                                "text": "This forces a structured, useful summary instead of a vague one.",
                                "prompt": "Summarize this document in 3 sections: 1) What changed/what's new, 2) Who is affected and how, 3) Any deadline or action required from me. Keep it under 150 words."
                            },
                            {
                                "title": "Verify critical details",
                                "text": "For anything affecting deadlines, pay, or rules — always double check the original document, don't rely only on the summary."
                            }
                        ],
                        "tip": "Works great for RTI replies too — paste the reply and ask 'did this RTI reply actually answer my original question fully?'"
                    },
                    {
                        "id": "gemini-translate",
                        "title": "Translate documents between English and Hindi/regional language accurately",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Official translation needs to preserve exact meaning, not casual conversation-style translation.",
                        "steps": [
                            {
                                "title": "Open Gemini",
                                "text": "Go to gemini.google.com — it handles Hindi and major Indian regional languages well."
                            },
                            {
                                "title": "Use this prompt for accuracy",
                                "text": "This ensures formal tone is preserved, not casual language.",
                                "prompt": "Translate the following official text into formal Hindi suitable for government documentation. Preserve technical and legal terms accurately, do not simplify or paraphrase. Text:"
                            },
                            {
                                "title": "Paste your text",
                                "text": "Add the original text right after the instruction."
                            },
                            {
                                "title": "Have someone verify if it's legally binding",
                                "text": "For any document with legal or policy weight, get the AI translation checked by a colleague fluent in both languages before official use."
                            }
                        ],
                        "tip": "Ask it to flag any words that don't have an exact translation, so you know where to double-check manually."
                    }
                ]
            },
            {
                "id": "ms_copilot",
                "title": "Microsoft Copilot",
                "icon": "📋",
                "description": "AI built directly into Word, Excel and Outlook",
                "lessons": [
                    {
                        "id": "copilot-getting-started",
                        "title": "What is Microsoft Copilot and where to find it",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "If your office uses Microsoft Office (Word, Excel, Outlook), Copilot is the built-in AI assistant inside those exact apps.",
                        "steps": [
                            {
                                "title": "Open Word, Excel, or Outlook",
                                "text": "Copilot appears as an icon in the ribbon at the top, usually on the right side."
                            },
                            {
                                "title": "Check if your office has a Copilot license",
                                "text": "Some features need a paid Microsoft 365 Copilot license — ask your IT department if you don't see the icon."
                            },
                            {
                                "title": "Click the Copilot icon in Word",
                                "text": "A side panel opens where you can type what you want it to help with."
                            },
                            {
                                "title": "Try a simple request",
                                "text": "Test it on a real but simple task first.",
                                "prompt": "Draft a one-paragraph summary of this document highlighting only the action items."
                            }
                        ],
                        "tip": "Copilot works best on documents that are already open in front of it — open the file first, then ask your question."
                    },
                    {
                        "id": "copilot-word-drafting",
                        "title": "Draft and rewrite official documents inside Word using Copilot",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Get a first draft started directly inside the document you're already working on, without switching to another app.",
                        "steps": [
                            {
                                "title": "Open a blank or existing Word document",
                                "text": "Click the Copilot icon in the ribbon."
                            },
                            {
                                "title": "Describe what you need",
                                "text": "Be specific about the document type and purpose.",
                                "prompt": "Draft a formal office circular announcing a change in working hours starting next month, in standard government office format."
                            },
                            {
                                "title": "Review the inserted draft",
                                "text": "Copilot writes directly into your document — read through it fully before keeping it."
                            },
                            {
                                "title": "Ask it to revise specific parts",
                                "text": "Select a paragraph and ask Copilot to 'make this more formal' or 'make this shorter' instead of rewriting everything yourself."
                            }
                        ],
                        "tip": "Always fact-check names, dates, and figures it inserts — Copilot doesn't know your actual case details unless you tell it."
                    },
                    {
                        "id": "copilot-outlook-email",
                        "title": "Manage your email inbox faster with Copilot in Outlook",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Summarize long email threads and draft replies without reading every single message in a chain.",
                        "steps": [
                            {
                                "title": "Open a long email thread in Outlook",
                                "text": "Look for the Copilot icon near the top of the email."
                            },
                            {
                                "title": "Click 'Summarize this thread'",
                                "text": "It gives you the key points of a long back-and-forth conversation in a few lines."
                            },
                            {
                                "title": "Ask it to draft a reply",
                                "text": "Click reply, then use Copilot to generate a first draft based on the thread.",
                                "prompt": "Draft a polite reply confirming receipt of this request and stating it will be processed within 7 working days."
                            },
                            {
                                "title": "Edit before sending",
                                "text": "Adjust tone or add specific details Copilot couldn't have known."
                            }
                        ],
                        "tip": "Use the thread summary feature especially for CC-heavy email chains where you were added late and need to catch up fast."
                    }
                ]
            },
            {
                "id": "excel_ai",
                "title": "Excel + AI",
                "icon": "📊",
                "description": "Use AI to write formulas and organize office data without learning Excel formulas by heart",
                "lessons": [
                    {
                        "id": "excel-ai-formulas",
                        "title": "Use AI to write Excel formulas for office data work",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Stop searching YouTube for formulas — describe what you want in plain language and get the exact formula.",
                        "steps": [
                            {
                                "title": "Open ChatGPT or Gemini",
                                "text": "Either works fine for this — you'll paste the formula into Excel afterward."
                            },
                            {
                                "title": "Describe your exact problem in plain words",
                                "text": "Mention column names exactly as they appear in your sheet.",
                                "prompt": "I have an Excel sheet with employee names in column A and attendance days in column B. Write a formula to highlight in red any employee with attendance below 20 days, and also give me a formula to count how many employees are below 20 days."
                            },
                            {
                                "title": "Copy the formula exactly",
                                "text": "Paste it into Excel exactly as given, including the = sign at the start."
                            },
                            {
                                "title": "Test on a copy first",
                                "text": "Always try new formulas on a duplicate sheet before applying to your real office data."
                            }
                        ],
                        "tip": "If the formula gives an error, paste the exact error message back to the AI and ask it to fix it — don't guess."
                    },
                    {
                        "id": "excel-copilot-builtin",
                        "title": "Use Microsoft Copilot directly inside Excel",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "If your office has Microsoft 365 Copilot, you can ask it questions about your actual data without writing any formula yourself.",
                        "steps": [
                            {
                                "title": "Open your Excel sheet as a proper table",
                                "text": "Select your data range and convert it to a Table (Insert > Table) — Copilot works best on properly formatted tables, not random scattered data."
                            },
                            {
                                "title": "Click the Copilot icon in the ribbon",
                                "text": "A side panel opens for your questions."
                            },
                            {
                                "title": "Ask questions about your data directly",
                                "text": "No formula writing needed — just ask in plain language.",
                                "prompt": "Which 5 employees have the highest number of leave days this year, and what is the average leave taken across the department?"
                            },
                            {
                                "title": "Ask it to create a chart",
                                "text": "Request a simple visual to present to your seniors, like 'create a bar chart of this data.'"
                            }
                        ],
                        "tip": "Double check any numbers Copilot reports against the raw data at least once — verify it's reading the correct columns."
                    },
                    {
                        "id": "excel-data-cleanup",
                        "title": "Clean up messy government data sheets using AI",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Old records often have inconsistent formatting (dates, names, spacing) — AI can help you spot and describe the cleanup needed.",
                        "steps": [
                            {
                                "title": "Identify the messy parts",
                                "text": "Look for inconsistent date formats, extra spaces, or mismatched capitalization in your sheet."
                            },
                            {
                                "title": "Describe the problem to ChatGPT or Gemini",
                                "text": "Ask for the specific Excel function, not a rewrite of your whole sheet.",
                                "prompt": "My Excel column has dates in mixed formats like '5/6/26', '05-06-2026', and 'June 5 2026'. Give me a formula or method to convert all of them into a single consistent DD-MM-YYYY format."
                            },
                            {
                                "title": "Apply the suggested method",
                                "text": "This is usually a formula, or a Find & Replace pattern, or 'Text to Columns' steps — follow exactly as given."
                            },
                            {
                                "title": "Spot-check the results",
                                "text": "Manually verify 5-10 random rows after cleanup to confirm nothing got corrupted."
                            }
                        ],
                        "tip": "Always keep a backup copy of the original file before running any bulk cleanup — mistakes in bulk edits are hard to undo."
                    }
                ]
            },
            {
                "id": "translation_ai",
                "title": "Translation & Language Tools",
                "icon": "🌐",
                "description": "Accurate translation for official documents and citizen communication",
                "lessons": [
                    {
                        "id": "translation-google-translate-vs-ai",
                        "title": "Google Translate vs ChatGPT/Gemini — which to use when",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Google Translate is faster for quick phrases, but AI chatbots give better results for formal, legally-worded documents.",
                        "steps": [
                            {
                                "title": "Use Google Translate for quick, short translations",
                                "text": "Good for single sentences, signage, or casual messages — instant and simple."
                            },
                            {
                                "title": "Use ChatGPT/Gemini for formal documents",
                                "text": "These let you specify tone and context, which Google Translate cannot do."
                            },
                            {
                                "title": "Try the same sentence in both",
                                "text": "Compare a formal sentence in both tools to see the difference in quality.",
                                "prompt": "Translate to formal Hindi: 'Your application has been forwarded to the concerned department for further necessary action.'"
                            },
                            {
                                "title": "Pick based on the stakes",
                                "text": "Higher-stakes official documents deserve the slower, more careful AI chatbot method."
                            }
                        ],
                        "tip": "Never use only Google Translate for anything legally binding — always have a human who knows both languages review it."
                    },
                    {
                        "id": "translation-citizen-communication",
                        "title": "Draft citizen-facing notices in multiple languages quickly",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "When a notice needs to go out in English plus one or more regional languages, AI can draft all versions at once consistently.",
                        "steps": [
                            {
                                "title": "Write or finalize the English version first",
                                "text": "This becomes your source text — get it fully correct before translating."
                            },
                            {
                                "title": "Ask for translation into multiple languages at once",
                                "text": "This keeps the tone and structure matching across all versions.",
                                "prompt": "Translate this public notice into formal Hindi and Marathi, keeping the same structure and tone in both. Notice: [paste your English notice here]"
                            },
                            {
                                "title": "Have a native speaker check each version",
                                "text": "For citizen-facing notices, accuracy matters — get someone fluent to review before publishing."
                            },
                            {
                                "title": "Keep all versions formatted identically",
                                "text": "Same headings, same notice number, same date format — only the language changes."
                            }
                        ],
                        "tip": "Ask the AI to flag any phrase that 'doesn't translate well directly' so you know exactly where to focus your manual review."
                    },
                    {
                        "id": "translation-technical-terms",
                        "title": "Handle technical and legal terms correctly across languages",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Some government and legal terms don't have a direct equivalent in regional languages — handle these carefully instead of accepting the first AI suggestion.",
                        "steps": [
                            {
                                "title": "Identify technical/legal terms in your document",
                                "text": "Things like 'affidavit', 'gazette notification', or specific scheme names."
                            },
                            {
                                "title": "Ask the AI specifically about those terms",
                                "text": "Don't just translate the whole document blindly — check tricky terms individually.",
                                "prompt": "What is the standard, officially accepted Hindi translation for 'affidavit' used in Indian government documents?"
                            },
                            {
                                "title": "Cross-check with official government glossaries",
                                "text": "Many departments have approved terminology lists — these override whatever the AI suggests."
                            },
                            {
                                "title": "Keep a personal glossary",
                                "text": "Save correct translations for terms you use often, so you don't have to re-verify every time."
                            }
                        ],
                        "tip": "When in doubt on a legal term, leave the English term in brackets next to the translation — this is common practice in official Indian documents."
                    }
                ]
            }
        ]
    },

### TECH EMPLOYEE PATH

    "tech_employee": {
        "display_name": "Tech Employee",
        "boxes": [
            {
                "id": "claude_code",
                "title": "Claude Code",
                "icon": "⌨️",
                "description": "The #1 AI coding agent in 2026 — works in your terminal, handles full tasks end to end",
                "lessons": [
                    {
                        "id": "claude-code-getting-started",
                        "title": "What is Claude Code and how to install it",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "Claude Code is an AI agent that runs in your terminal — you give it a task, it reads your files, makes a plan, edits code across multiple files, and runs tests itself.",
                        "steps": [
                            {
                                "title": "Open your terminal",
                                "text": "On Windows use PowerShell or VS Code's built-in terminal."
                            },
                            {
                                "title": "Install it via npm",
                                "text": "Run this command (needs Node.js installed first):",
                                "prompt": "npm install -g @anthropic-ai/claude-code"
                            },
                            {
                                "title": "Navigate to your project folder",
                                "text": "Use 'cd your-project-folder' in the terminal, then type 'claude' to start it."
                            },
                            {
                                "title": "Give it a small first task",
                                "text": "Start simple to see how it works before trying anything complex.",
                                "prompt": "Add a docstring to every function in this file explaining what it does."
                            }
                        ],
                        "tip": "Always review what it changed using 'git diff' before committing — treat it like a junior developer's pull request, not a blind copy-paste."
                    },
                    {
                        "id": "claude-code-bug-fix",
                        "title": "Fix a bug end-to-end using Claude Code",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Instead of manually tracing through files to find a bug, describe the symptom and let it investigate.",
                        "steps": [
                            {
                                "title": "Make sure your project is in a git repo",
                                "text": "This lets you easily undo changes if needed — run 'git status' to confirm."
                            },
                            {
                                "title": "Describe the actual bug, not the fix",
                                "text": "Give symptoms and exact error messages, let it find the root cause.",
                                "prompt": "Users report that clicking 'submit' on the signup form sometimes does nothing. Here's the error from the console: [paste error]. Find the root cause and fix it."
                            },
                            {
                                "title": "Let it read relevant files first",
                                "text": "It will explore your codebase automatically — this can take a minute on larger projects."
                            },
                            {
                                "title": "Review the diff before accepting",
                                "text": "Check 'git diff' to see exactly what changed across all files before committing."
                            }
                        ],
                        "tip": "If it over-engineers a simple fix, explicitly say 'keep this as minimal as possible, don't refactor unrelated code.'"
                    },
                    {
                        "id": "claude-code-write-tests",
                        "title": "Auto-generate unit tests for your functions",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Writing test cases is repetitive and often skipped under deadline pressure — automate the boring part.",
                        "steps": [
                            {
                                "title": "Point it at a specific file or function",
                                "text": "Be specific about scope so it doesn't try to test your entire codebase at once."
                            },
                            {
                                "title": "Ask for tests with edge cases included",
                                "text": "This ensures it covers edge cases, not just the happy path.",
                                "prompt": "Write unit tests for the validateEmail function in utils/validators.js using Jest. Include normal cases, edge cases, and invalid input cases."
                            },
                            {
                                "title": "Let it run the tests itself",
                                "text": "Claude Code can execute the test suite and see if they pass — it will fix failing tests automatically if you ask."
                            },
                            {
                                "title": "Review failures carefully",
                                "text": "Some generated tests might fail due to assumptions about your code — read failures carefully, they often reveal real bugs."
                            }
                        ],
                        "tip": "Ask it to add a comment above each test explaining what specific case it's checking — makes the test file much easier for teammates to read."
                    }
                ]
            },
            {
                "id": "github_copilot",
                "title": "GitHub Copilot",
                "icon": "🤖",
                "description": "Inline autocomplete inside your editor as you type — the most widely adopted coding AI",
                "lessons": [
                    {
                        "id": "copilot-setup",
                        "title": "Set up GitHub Copilot properly in VS Code",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "Copilot autocompletes code as you type — most people install it but never configure it to actually work well.",
                        "steps": [
                            {
                                "title": "Open VS Code Extensions panel",
                                "text": "Press Ctrl+Shift+X, search for 'GitHub Copilot.'"
                            },
                            {
                                "title": "Install and sign in",
                                "text": "Click Install, then sign in with your GitHub account when prompted. Needs an active Copilot subscription (free trial available)."
                            },
                            {
                                "title": "Write a clear comment before coding",
                                "text": "Type a comment describing what you want, like: // function to validate email format using regex — Copilot suggests code based on this."
                            },
                            {
                                "title": "Press Tab to accept suggestions",
                                "text": "Suggestions appear in grey text — press Tab to accept, or keep typing to ignore."
                            }
                        ],
                        "tip": "Write more detailed comments for better suggestions — 'sort array' gives generic code, 'sort array of user objects by signup date descending' gives much more accurate code."
                    },
                    {
                        "id": "copilot-chat",
                        "title": "Use Copilot Chat to ask questions about your code inline",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Beyond autocomplete, Copilot has a chat panel for asking questions without leaving your editor.",
                        "steps": [
                            {
                                "title": "Open Copilot Chat panel",
                                "text": "Click the chat icon in VS Code's sidebar, or press Ctrl+Alt+I."
                            },
                            {
                                "title": "Select code, then ask about it",
                                "text": "Highlight a confusing block of code first, then ask your question — it uses the selection as context.",
                                "prompt": "Explain what this function does and why it might be slow on large inputs."
                            },
                            {
                                "title": "Ask it to explain an error",
                                "text": "Paste a terminal error directly into the chat and ask what's causing it."
                            },
                            {
                                "title": "Use slash commands",
                                "text": "Try typing '/fix' or '/tests' in the chat — these are shortcuts for common requests."
                            }
                        ],
                        "tip": "Use Chat for understanding and discussion, and inline autocomplete (Tab) for actually writing the code — they're better at different jobs."
                    },
                    {
                        "id": "copilot-coding-agent",
                        "title": "Assign a GitHub issue to Copilot's coding agent",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Copilot can now work autonomously on a GitHub issue — creating a branch, writing the code, and opening a pull request by itself.",
                        "steps": [
                            {
                                "title": "Open an issue in your GitHub repository",
                                "text": "Make sure the issue clearly describes what needs to be done."
                            },
                            {
                                "title": "Assign it to Copilot",
                                "text": "Look for the assignee field and select 'Copilot' instead of a human teammate."
                            },
                            {
                                "title": "Wait for the pull request",
                                "text": "Copilot will create a branch, write code, run tests, and open a PR automatically — this can take several minutes."
                            },
                            {
                                "title": "Review the PR like any teammate's work",
                                "text": "Read the full diff, run it locally if needed, and request changes before merging — never auto-merge AI-generated PRs without review."
                            }
                        ],
                        "tip": "Best for well-defined, smaller issues — avoid assigning vague or massive issues until you've tested it on simpler ones first."
                    }
                ]
            },
            {
                "id": "chatgpt",
                "title": "ChatGPT",
                "icon": "💬",
                "description": "Best for architecture discussions, debugging, and explaining unfamiliar technologies",
                "lessons": [
                    {
                        "id": "chatgpt-debug-errors",
                        "title": "Debug confusing error messages fast using ChatGPT",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "Stop spending an hour on Stack Overflow for one error — get a direct explanation and fix.",
                        "steps": [
                            {
                                "title": "Copy the full error message",
                                "text": "Include the entire stack trace/error output, not just the last line."
                            },
                            {
                                "title": "Paste it with this prompt",
                                "text": "This gets you an explanation, not just a fix to blindly copy.",
                                "prompt": "I'm getting this error in [language/framework]. Explain in simple terms why this is happening, then give me the fix. Error:"
                            },
                            {
                                "title": "Mention your language/framework",
                                "text": "Replace the bracket with what you're using, e.g. 'Python Flask' or 'React JavaScript'."
                            },
                            {
                                "title": "Understand before copying",
                                "text": "Read the explanation first — if you don't understand why it happened, ask 'explain this like I'm new to this concept' before applying the fix."
                            }
                        ],
                        "tip": "If the first fix doesn't work, paste the new error you get — don't start a new chat, keep the context going for faster debugging."
                    },
                    {
                        "id": "chatgpt-architecture-discussion",
                        "title": "Use ChatGPT to think through system architecture decisions",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Before writing any code, talk through your design choices with AI to catch problems early — much cheaper than refactoring later.",
                        "steps": [
                            {
                                "title": "Describe your actual requirements",
                                "text": "Include scale, constraints, and what matters most (speed, cost, simplicity)."
                            },
                            {
                                "title": "Ask for tradeoffs, not just one answer",
                                "text": "This avoids getting a single confident-sounding suggestion that may not fit your actual needs.",
                                "prompt": "I'm building a notification system that needs to handle 10,000 events per minute. Compare using a message queue (like RabbitMQ) vs a simple database polling approach. What are the tradeoffs for a small team with no dedicated DevOps?"
                            },
                            {
                                "title": "Push back and ask follow-ups",
                                "text": "Treat it like a conversation with a colleague — challenge its assumptions if something doesn't fit your real constraints."
                            },
                            {
                                "title": "Make the final decision yourself",
                                "text": "Use it to surface options and tradeoffs, but the final architectural decision and accountability stays with you and your team."
                            }
                        ],
                        "tip": "Ask it to argue against its own first suggestion — this often surfaces hidden weaknesses you wouldn't have thought to ask about."
                    },
                    {
                        "id": "chatgpt-learn-new-tech",
                        "title": "Quickly get up to speed on an unfamiliar technology or codebase",
                        "updated": "June 2026",
                        "time": "3 min",
                        "intro": "When you're suddenly asked to work with a framework or language you've never used, get a fast practical orientation instead of reading docs for hours.",
                        "steps": [
                            {
                                "title": "State your existing background",
                                "text": "This helps it calibrate the explanation to your actual level, not too basic or too advanced."
                            },
                            {
                                "title": "Ask for a practical orientation, not theory",
                                "text": "Focus on what you'll actually need to be productive quickly.",
                                "prompt": "I'm an experienced Python developer who has never used Go. Give me the 10 most important differences I need to know to read and write basic Go code, assuming I already understand programming concepts."
                            },
                            {
                                "title": "Ask for a small practice task",
                                "text": "Request a tiny hands-on exercise to actually try the new syntax yourself."
                            },
                            {
                                "title": "Keep the chat open while working",
                                "text": "Return to ask follow-up questions as you encounter real confusion in the actual codebase."
                            }
                        ],
                        "tip": "Ask it to specifically list 'common mistakes developers from [your old language] make when switching to [new language]' — this catches habit-based bugs early."
                    }
                ]
            },
            {
                "id": "cursor",
                "title": "Cursor",
                "icon": "🖱️",
                "description": "A full AI-first code editor that understands your entire codebase, not just one file",
                "lessons": [
                    {
                        "id": "cursor-getting-started",
                        "title": "What is Cursor and how to install it",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Cursor is a complete code editor (built on VS Code) where AI understands your whole project, not just the open file.",
                        "steps": [
                            {
                                "title": "Go to cursor.com and download it",
                                "text": "Available for Windows, Mac, and Linux."
                            },
                            {
                                "title": "Install and open your project folder",
                                "text": "It looks and feels almost identical to VS Code, so your existing shortcuts mostly still work."
                            },
                            {
                                "title": "Open the AI chat panel",
                                "text": "Press Ctrl+L to open the chat sidebar."
                            },
                            {
                                "title": "Ask a question about your whole project",
                                "text": "Notice it can answer using context from multiple files automatically.",
                                "prompt": "Where in this codebase is user authentication handled, and how does it work?"
                            }
                        ],
                        "tip": "If you have existing VS Code extensions and settings, Cursor can usually import them automatically on first setup."
                    },
                    {
                        "id": "cursor-composer-multifile",
                        "title": "Use Composer to make changes across multiple files at once",
                        "updated": "June 2026",
                        "time": "5 min",
                        "intro": "Instead of manually editing file after file for one feature, describe the whole change and let it edit everything together.",
                        "steps": [
                            {
                                "title": "Open Composer",
                                "text": "Press Ctrl+I to open the Composer panel."
                            },
                            {
                                "title": "Describe the full feature or change",
                                "text": "Be specific about what should happen across the affected files.",
                                "prompt": "Add a 'dark mode' toggle. Add a button in the header component, store the preference in local storage, and apply a dark theme class to the app's root element when enabled."
                            },
                            {
                                "title": "Review each file change before applying",
                                "text": "Composer shows proposed changes per file — review each one rather than accepting all blindly."
                            },
                            {
                                "title": "Test the feature manually",
                                "text": "Run your app and actually click the new feature to confirm it works as expected."
                            }
                        ],
                        "tip": "For large or risky changes, commit your current work to git first so you have a clean point to revert to if Composer's changes don't work out."
                    },
                    {
                        "id": "cursor-refactor-codebase",
                        "title": "Refactor a messy part of your codebase using Cursor",
                        "updated": "June 2026",
                        "time": "4 min",
                        "intro": "Cursor's whole-codebase awareness makes it especially good at consistent refactors across many files.",
                        "steps": [
                            {
                                "title": "Identify the specific pattern to refactor",
                                "text": "Be precise — vague refactor requests on a full codebase can go wrong quickly."
                            },
                            {
                                "title": "Reference the specific files or pattern",
                                "text": "Use the @ symbol in Cursor to directly reference specific files for it to focus on.",
                                "prompt": "@UserController.js @OrderController.js These two files both implement pagination differently. Refactor both to use a shared pagination utility function with the same behavior."
                            },
                            {
                                "title": "Review the diff carefully",
                                "text": "Multi-file refactors are exactly where small mistakes hide — check each changed file individually."
                            },
                            {
                                "title": "Run your full test suite",
                                "text": "Don't just eyeball the code — actually run tests to confirm nothing broke across the codebase."
                            }
                        ],
                        "tip": "Cursor can get sluggish on very large codebases (100K+ lines) — for huge refactors, consider doing them in smaller batches by module."
                    }
                ]
            }
        ]
    }
}