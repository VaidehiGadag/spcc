#include <stdio.h>

void optimizedCode() {
    // Constant Folding: Precompute sum at compile-time
    printf("Sum: %d\n", 30); // 10 + 20 is replaced directly

    // Dead Code Elimination: Removed unused variable 'y'

    // Strength Reduction: Replace multiplication with bitwise shift
    int i;
    for (i = 0; i < 10; i++) {
        int result = i << 1; // i * 2 is replaced with i << 1
        printf("%d ", result);
    }
    printf("\n");

    // Loop Unrolling: Reduce loop iterations by processing multiple elements at once
    int arr[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    for (i = 0; i < 8; i += 2) {
        arr[i] = arr[i] * 2;
        arr[i + 1] = arr[i + 1] * 2; // Process two elements per iteration
    }

    // Printing the updated array
    printf("Updated array: ");
    for (i = 0; i < 8; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Loop Jamming: Merge loops to reduce iteration overhead
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5] = {6, 7, 8, 9, 10};
    int arr3[5], arr4[5];

    for (i = 0; i < 5; i++) {
        arr3[i] = arr1[i] + 2;
        arr4[i] = arr2[i] * 3; // Merged into a single loop
    }

    // Printing arr3 and arr4
    printf("arr3: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr3[i]);
    }
    printf("\n");

    printf("arr4: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr4[i]);
    }
    printf("\n");
}

int main() {
    optimizedCode();
    return 0;
}