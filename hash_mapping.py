from entry import Entry


class HashMapping:
    """Mapping ADT that stores key value pairs in buckets using separate chaining"""
    def __init__(self, size=2):
        """Initializes an empty HashMapping with size buckets"""
        self._n_buckets = max(1, size)
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def __len__(self):
        """Returns the number of key value pairs in the HashMapping"""
        return self._len

    def _find_bucket(self, key):
        """Returns the index of the bucket key should go in, based on hash(key) and the number of buckets"""
        return hash(key) % self._n_buckets

    def __contains__(self, key):
        """Returns True (False) if key is (is not) in the HashMapping"""
        bucket = self._L[self._find_bucket(key)]
        for entry in bucket:
            if entry.key == key:
                return True
        return False

    def put(self, key, value):
        """Adds a new key value pair or updates the value for an existing key"""
        bucket = self._L[self._find_bucket(key)]

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(Entry(key, value))
        self._len += 1

        if len(self) >= 2 * self._n_buckets:
            self._rehash(2 * self._n_buckets)

    def get(self, key):
        """Returns the value for key, raises a KeyError if the key is not present"""
        bucket = self._L[self._find_bucket(key)]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        raise KeyError(f"Tried to get nonexistent key {key}")

    def rehash(self):
        """Doubles the bucket table and reinserts every existing entry"""
        self._rehash(2 * self._n_buckets)

    def _rehash(self, new_buckets):
        """Rehashes every entry from a table with the current bucket count to one with new_buckets"""
        self._n_buckets = new_buckets
        new_li = [[] for i in range(new_buckets)]

        for bucket in self._L:
            for entry in bucket:
                new_idx = self._find_bucket(entry.key)
                new_li[new_idx].append(entry)

        self._L = new_li