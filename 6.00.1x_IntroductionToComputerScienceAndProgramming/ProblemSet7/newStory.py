class NewsStory(object):
    """
    """
    def __init__(self, storyGuid, storyTitle, storySubject,
                 storySummary, storyLink):
        """
        Arguments:
        - `storyTitle`:
        - `storySubject`:
        - `storySummary`:
        - `storyURL`:
        """
        self._storyGuid = storyGuid
        self._storyTitle = storyTitle
        self._storySubject = storySubject
        self._storySummary = storySummary
        self._storyLink = storyLink

    def getGuid(self):
        """
        """
        return self._storyGuid

    def getTitle(self):
        """
        """
        return self._storyTitle

    def getSubject(self):
        """
        """
        return self._storySubject

    def getSummary(self):
        """
        """
        return self._storySummary

    def getLink(self):
        """
        """
        return self._storyLink
