class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):

    def __init__(self, word):
        """

        Arguments:
        - `word`:
        """
        self._word = word
        self.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    def isWordIn(self, text):
        """
        """
        whitespace = " "
        replacedStr = text
        upperWord = self._word.upper()
        for char in self.punctuation:
            replacedStr = replacedStr.replace(char, whitespace)
        splited = replacedStr.split(whitespace)
        for word in splited:
            if word.upper() == upperWord:
                return True
        return False


class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())


class SubjectTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


class NotTrigger(Trigger):

    def __init__(self, anotherTrigger):
        self._anotherTrigger = anotherTrigger

    def evaluate(self, story):
        return (not self._anotherTrigger.evaluate(story))


class AndTrigger(Trigger):
    """
    """

    def __init__(self, t1, t2):
        """

        Arguments:
        - `triggerOne`:
        - `triggerTwo`:
        """
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)


class OrTrigger(Trigger):
    """
    """
    def __init__(self, t1, t2):
        """
        Arguments:
        - `t1`:
        - `t2`:
        """
        self._t1 = t1
        self._t2 = t2

    def evaluate(self, story):
        """
        """
        return self._t1.evaluate(story) or self._t2.evaluate(story)


class PhraseTrigger(Trigger):
    """
    """

    def __init__(self, phrase):
        """
        """
        self._phrase = phrase

    def evaluate(self, story):
        inTitle = self._phrase in story.getTitle()
        if (inTitle):
            return True
        inSubject = self._phrase in story.getSubject()
        if (inSubject):
            return True
        inSummary = self._phrase in story.getSummary()
        if (inSummary):
            return True
        return False


def filterStories(stories, triggerList):
    result = []
    for story in stories:
        for trigger in triggerList:
            if trigger.evaluate(story):
                result.append(story)
                break
    return result


