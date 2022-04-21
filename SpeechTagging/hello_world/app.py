import json
import nltk


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    sentence = event['sentence']
    tokens = nltk.word_tokenize(sentence)
    outputs = nltk.pos_tag(tokens)
    
    explanations = {
        'CC':'coordinating conjunction',
        'CD':'cardinal digit',
        'DT':'determiner',
        'EX':'existential there',
        'FW':'foreign word',
        'IN':'preposition/subordinating conjunction',
        'JJ':'This NLTK POS Tag is an adjective (large)',
        'JJR':'adjective, comparative (larger)',
        'JJS':'adjective, superlative (largest)',
        'LS':'list market',
        'MD':'modal (could, will)',
        'NN':'noun, singular (cat, tree)',
        'NNS':'noun plural (desks)',
        'NNP':'proper noun, singular (sarah)',
        'NNPS':'proper noun, plural (indians or americans)',
        'PDT':'predeterminer (all, both, half)',
        'POS':'possessive ending (parent\ ‘s)',
        'PRP':'personal pronoun (hers, herself, him, himself)',
        'PRP$':'possessive pronoun (her, his, mine, my, our)',
        'RB':'adverb (occasionally, swiftly)',
        'RBR':'adverb, comparative (greater)',
        'RBS':'adverb, superlative (biggest)',
        'RP':'particle (about)',
        'TO':'infinite marker (to)',
        'UH':'interjection (goodbye)',
        'VB':'verb (ask)',
        'VBG':'verb gerund (judging)',
        'VBD':'verb past tense (pleaded)',
        'VBN':'verb past participle (reunified)',
        'VBP':'verb, present tense not 3rd person singular(wrap)',
        'VBZ':'verb, present tense with 3rd person singular (bases)',
        'WDT':'wh-determiner (that, what)',
        'WP':'wh- pronoun (who)',
        'WRB':'wh- adverb (how)'
    }
    
    expanded_outputs = []
    for token, pos_tag in outputs:
        if pos_tag in explanations:
            expanded_outputs.append((token, explanations[pos_tag]))
    print(json.dumps(expanded_outputs, indent=4))
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "results": json.dumps(expanded_outputs, indent=4)
            }
        ),
    }
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps(
    #         {
    #             "message": "hello world",
    #         }
    #     ),
    # }