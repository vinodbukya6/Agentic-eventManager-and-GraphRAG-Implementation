# Map-reduce style query answering
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import OPENAI_MODEL
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name=OPENAI_MODEL, temperature=0)

# scoring prompt where we discard irrelevant answers generated from each summaries
scoring_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template="""
    You are given a user's question and an answer generated from a community summary.
    Question: {query}
    Answer: {answer}
    Rate the relevance of the answer on a scale from 0 (completely irrelevant) to 5 (highly relevant). 
    Respond ONLY with a single number (0 to 5).
    """
    )

def score_answer(query, answer):
    #score_str = llm.invoke(scoring_prompt.format(query=query, answer=answer)).strip()
    response = llm.invoke(scoring_prompt.format(query=query, answer=answer))
    score_str = response.content.strip()
    try:
        return int(score_str)
    except:
        return 0  # fallback if parsing fails

def answer_query(query, community_summaries, score_threshold=3):
    partials = []
    for cid, summary in community_summaries.items():
        #print(summary)
        # Community wise partial answers
        prompt = (
            f"You are an expert assistant. Based only on the following community summary, answer the user's question as clearly and concisely as possible. "
            f"If the summary is not relevant, reply 'Not relevant'.\n\n"
            f"Community Summary:\n{summary}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )
        #answer = llm.predict(prompt)
        result = llm.invoke(prompt)
        answer = result.content if hasattr(result, 'content') else result
        #print(result)

        # relevance score
        score = score_answer(query, answer)
        if score >= score_threshold:
            partials.append((cid, answer))

    if not partials:
        return "No relevant information found in the document." 
    # 
    #print(partials[0])    
    # use above partial summaries to answer final response 
    final_prompt = (
        "You are an expert assistant. Given the following partial answers from different communities, synthesize a single, comprehensive, and well-structured answer to the user's question. "
        "Deduplicate information, resolve conflicts, and ensure clarity. Reference the original question and do not include irrelevant information.\n\n"
        f"Question: {query}\n\n"
        "Partial Answers:\n"
        + "\n---\n".join([a for _, a in partials])
        + "\n\nFinal Answer:"
    )
    
    final_answer = llm.invoke(final_prompt)
    if hasattr(final_answer, 'content'):
        final_answer = final_answer.content
    return final_answer
    #return llm.invoke(final_prompt)
