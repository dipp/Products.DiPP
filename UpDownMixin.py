class UpDownMixin:
        def moveObjectsByDelta(self, ids, delta, subset_ids=None):
                return 0

        def moveObjectsUp(self, ids, delta=1):
                if not isinstance(ids, list):
                        self.move_object_up(ids)
                        return 1
                for id in ids:
                        for i in range(delta):
                                self.move_object_up(id)

                return len(ids)

        def moveObjectsDown(self, ids, delta=1):
                if not isinstance(ids, list):
                        self.move_object_down(ids)
                        return 1
                for id in ids:
                        for i in range(delta):
                                self.move_object_down(id)

                return len(ids)

        def moveObjectsToTop(self, ids):
                for id in ids:
                        self.move_object_to_top(id)

                return len(ids)

        def moveObjectsToBottom(self, ids):
                for id in ids:
                        self.move_object_to_bottom(id)

                return len(ids)

        def orderObjects(self, key, reverse=None):
                return 0

        def getObjectPosition(self, id):
                return self.get_object_position(id)

        def moveObjectToPosition(self, id, position):
                origpos = self.get_object_position(id)
                self.move_object_to_position(id, position)

                return abs(position - origpos)
