# set up the ollama with medgemma tool
import ollama
from config import OPENAI_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def query_medgemma(prompt:str) -> str:
    
    """
    Calls MedGemma Model with a therapist personality profile.
    Return responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist.
     Respond to patients with :
    
    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when ...")
    3. Practical guidance ("What sometimes helps is ...")
    4. Strengths-focused support ("I notice how you're really strong at ...")
    
    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep th conversation going by asking open ended questions to dive intp root cause of patients problem
    """
     
    try :
        response = ollama.chat(
            model = 'alibayram/medgemma:4b',
            messages = [
                {"role":"system","content":system_prompt,},
                {"role":"user","content":prompt,},
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."
    
    
#setup twilio calling api tool
from twilio.rest import Client

def call_emergency(phone:str):
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=EMERGENCY_CONTACT,
        from_=TWILIO_FROM_NUMBER
    )
    
