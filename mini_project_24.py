"""
Build a TriageQueue class on top of the PriorityQueue pattern from Concept 6. Patients arrive as 
(name, severity), where severity 1 = most critical and severity 5 = least critical. When two patients 
share the same severity, the one who arrived FIRST must be treated first — this needs a tie-breaker, 
not just the severity number. Feed in at least eight patients in a mixed, non-sorted order, then pop and 
print the full treatment order. Confirm by hand that both the severity rule and the tie-breaking rule 
were respected
"""

import heapq
class TriageQueue:
    def __init__(self):
        self.heap = []
        self.countr = 0
    def add_patient(self, name, severity):
        arrival_order = self.countr
        self.countr += 1
        patient = (severity, arrival_order, name)
        heapq.heappush(self.heap, patient)
    def treat_next(self):
        if not self.heap:
            return None
        severity, arreival_order, name = heapq.heappop(self.heap)
        return name, severity
queue = TriageQueue()
queue.add_patient("Ahmed", 4)
queue.add_patient("Mona", 2)
queue.add_patient("Ali", 5)
queue.add_patient("Sara", 1)
queue.add_patient("Omar", 3)
queue.add_patient("Hanan", 2)
queue.add_patient("Youssef", 1)
queue.add_patient("Layla", 3)
while queue.heap:
    patient = queue.treat_next()
    print(patient)

