# Unittests and Integration Tests

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

-The difference between unit and integration tests.
-Common testing patterns such as mocking, parametrizations and fixtures

#Unit Tests vs. Integration Tests:
##Unit Tests:

Focuses on testing individual units or components of code in isolation.
Isolates a specific piece of code (function, method, class) and verifies its behavior.
Mocks or stubs external dependencies to isolate the unit being tested.
Helps ensure that each unit of the software functions as expected.
Integration Tests:

Focuses on testing the interaction between different units or components.
Validates the integration of multiple units or modules to ensure they work together as intended.
May involve testing databases, APIs, file systems, or external services.
Ensures the interoperability and collaboration between various parts of the system.
Common Testing Patterns:

##Mocking:

Technique to replace parts of the system with simulated objects (mocks) that mimic the behavior of real objects.
Useful for isolating the code under test from its dependencies, making tests faster and more focused.
Allows testing interactions with external systems without actually involving them.

## Parametrization:

A way to run the same test code with multiple sets of data.
Enables testing different scenarios using a single test method, improving test coverage.

## Fixtures:

Pre-defined states or objects used as a baseline for running tests.
Set up and initialize test environments or objects before running the tests.
Ensures consistency and repeatability of tests by providing a known starting point.


# Resources
Read or watch:

-[unittest — Unit testing framework](https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA)
-[unittest.mock — mock object library](https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA)
-[How to mock a readonly property with mock?](https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q)
-[parameterized](https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg)
-[Memoization](https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA)
