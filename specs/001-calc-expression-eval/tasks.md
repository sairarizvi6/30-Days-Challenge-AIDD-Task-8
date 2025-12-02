# Tasks: Calculator Expression Evaluation

**Input**: Design documents from `/specs/001-calc-expression-eval/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `src/calculator/` and `src/history/` directories
- [ ] T002 Initialize Python project with basic structure (e.g., `__init__.py` files)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 Configure basic error handling and logging infrastructure in `src/utils/errors.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Evaluate Mathematical Expression (Priority: P1) 🎯 MVP

**Goal**: Allow users to input a mathematical expression, validate it, evaluate it, handle errors, store it in history, and return a formatted result.

**Independent Test**: Can be fully tested by providing a valid mathematical expression (e.g., "2 + 3 * 4"), an invalid one (e.g., "2 + * 3"), and an expression with division by zero (e.g., "1 / 0"), and observing the correct result or error message.

### Implementation for User Story 1

- [ ] T004 [US1] Implement input sanitization in `src/calculator/input_sanitizer.py`
- [ ] T005 [US1] Implement mathematical expression validation in `src/calculator/expression_validator.py`
- [ ] T006 [US1] Implement parsing of operators and operands (e.g., using a shunting-yard algorithm) in `src/calculator/expression_parser.py`
- [ ] T007 [US1] Implement expression evaluation with operator precedence and parentheses support in `src/calculator/expression_evaluator.py`
- [ ] T008 [US1] Enhance error handling for division by zero and invalid syntax within `src/calculator/expression_evaluator.py`
- [ ] T009 [US1] Implement a history manager to store calculations in `src/history/calculator_history.py`
- [ ] T010 [US1] Implement result formatting in `src/calculator/result_formatter.py`
- [ ] T011 [US1] Create a main calculator interface to orchestrate input, validation, parsing, evaluation, history, and output in `src/calculator/main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T012 Code cleanup and refactoring in `src/calculator/` and `src/history/`

---

## Phase X: Streamlit Integration

**Purpose**: Provide a web-based user interface for the calculator using Streamlit.

- [ ] T013 Install Streamlit library (`pip install streamlit`)
- [ ] T014 Create Streamlit application interface in `src/app.py`
- [ ] T015 Integrate calculator logic into `src/app.py`
- [ ] T016 Run Streamlit application on local host

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete
- **Streamlit Integration (Phase X)**: Depends on Polish (Final Phase) completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members
- Streamlit Integration tasks are sequential and depend on prior tasks.

---

## Parallel Example: User Story 1

```bash
# All tasks within User Story 1 are largely sequential due to dependencies on each other.
# However, if some sub-components (e.g., different types of validators) could be developed in separate files,
# those could be parallelized.
# For example, if T004, T005, T006, T007 were split into smaller, independent components.
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
