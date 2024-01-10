#include "stdio.h"

void test_help()
{
    printf("Available tests:\n"

           "    test config                         show configuration\n"
           "    test hash <s1> <s2> ...             compute hash of strings s1, s2, ...\n"
           "    test c2i <c1> <c2> ...              compute c2i(c1), c2i(c2), ...\n"
           "    test i2c <i1> <i2> ...              compute i2c(i1), i2c(i2), ...\n"
           "    test h2i <s> <t> [n]                compute h2i(H(s), t, n)\n"
           "    test i2i <i1> <t1> ...              compute i2i(i1, t1), i2i(i2, t2), ...\n"
           "    test time_i2i [N]                   compute average time of single i2i call over N calls\n"
           "    test full_chain <width> <i1> ...    compute (full) chains starting at i1, i2, ...\n"
           "    test FULL_chain <width> <i1> ...    compute (full, with details) chains starting at i1, i2, ...\n"
           "    test chain <w1> <i1> <w2> <i2> ...  compute chains starting at i1, i2, ..., of length w1, w2, ...\n"
           "    test search <FILENAME> <i>          search the first and last occurences of i in table\n"
           "    test list                           this list\n");
}

int test_hash(int argc, char* argv[])
{
    if (argc == 0) {
        printf("wrong number of arguments\n");
        return 1;
    }
    printf("fonction de hash = %s\n\n", HASH[CFG.hash_nb]);
    char* clear;
    for (int i = 0; i < argc; i++) {
        clear = argv[i];
        hash(clear, _hash);
        for (int k = 0; k < CFG.hash_size; k++) {
            printf("%02X", _hash[k]);
        }
        printf("  (%s)\n", clear);
    }
    return 0;
}

int test_time_i2i(int argc, char* argv[])
{
    int n;
    if (argc > 1) {
        printf("wrong number of arguments\n");
        return 1;
    }
    if (argc == 0) {
        n = 1000000;
    } else {
        n = atoi(argv[0]);
    }
    double t = time_hash(n);
    printf("fonction de hash = %s\n\n", HASH[CFG.hash_nb]);
    printf("%fs pour %i appels à i2i, ie %fμs par appel\n", t, n, 1000000 * t / n);
    return 0;
}

int test_config(int argc, char* argv[])
{
    (void)argv;
    if (argc != 0) {
        printf("wrong number of arguments\n");
        return 1;
    }
    show_CFG(1);
    return 0;
}

int test_i2c(int argc, char* argv[])
{
    if (argc == 0) {
        printf("wrong number of arguments\n");
        return 1;
    }

    show_CFG(0);
    for (int i = 0; i < argc; i++) {
        u64 idx = atoll(argv[i]);
        char clear[64];
        i2c(idx, clear);
        printf("i2c(%" PRIu64 ") = \"%s\"\n", idx, clear);
    }
    return 0;
}

int test_c2i(int argc, char* argv[])
{
    if (argc == 0) {
        printf("wrong number of arguments\n");
        return 1;
    }

    show_CFG(0);
    for (int i = 0; i < argc; i++) {
        u64 idx = c2i(argv[i]);
        printf("c2i(%s) = %" PRIu64 "\n", argv[i], idx);
    }
    return 0;
}

int test_h2i(int argc, char* argv[])
{
    if (argc != 2 && argc != 3) {
        printf("wrong number of arguments\n");
        return 1;
    }
    char* s = argv[0];
    int t = atoi(argv[1]);
    int n = 0;
    if (argc == 3) {
        n = atoi(argv[2]);
    }

    show_CFG(1);

    hash(s, _hash);

    printf("hash(\"%s\") = ", s);
    for (int j = 0; j < CFG.hash_size; j++) {
        printf("%02x", _hash[j]);
    }
    printf("\n");

    if (n == 0) {
        printf("h2i(hash(\"%s\"), %d) = %lu\n", s, t, h2i(_hash, t, 0));
    } else {
        printf("h2i(hash(\"%s\"), %d, %d) = %lu\n", s, t, n, h2i(_hash, t, n));
    }

    return 0;
}

int test_i2i(int argc, char* argv[])
{
    if (argc < 1) {
        printf("wrong number of arguments\n");
        return 1;
    }

    show_CFG(1);

    u64 idx;
    u64 t;
    for (int i = 0; i < argc; i += 2) {
        idx = strtoull(argv[i], NULL, 10);
        if (i + 1 < argc) {
            t = strtoull(argv[i + 1], NULL, 10);
        } else {
            t = 0;
        }
        i2c(idx, _clear);
        printf("%" PRIu64 " --i2c--> %s ", idx, _clear);
        hash(_clear, _hash);
        printf("--h--> ");
        for (int j = 0; j < CFG.hash_size; j++) {
            printf("%02x", _hash[j]);
        }
        printf(" --h2i(%" PRIu64 ")--> %" PRIu64 "\n", t, h2i(_hash, t, 0));
        printf("%" PRIu64 "  --i2i(%" PRIu64 ")-->  %" PRIu64 "\n", idx, t, i2i(idx, t, 0));
        printf("\n");
    }
    return 0;
}

int test_full_chain(int argc, char* argv[])
{
    if (argc < 2) {
        printf("wrong number of arguments\n");
        return 1;
    }
    int width = atoi(argv[0]);
    argv++;
    argc--;
    show_CFG(1);

    u64 idx;
    for (int i = 0; i < argc; i++) {
        idx = strtoull(argv[i], NULL, 10);
        printf("%" PRIu64, idx);
        for (int j = 1; j < width; j++) {
            idx = i2i(idx, j, 0);
            printf("\n   --i2i(%i)--> %" PRIu64, j, idx);
        }
        printf("\n\n");
    }
    return 0;
}

int test_FULL_chain(int argc, char* argv[])
{
    if (argc < 2) {
        printf("wrong number of arguments\n");
        return 1;
    }
    int width = atoi(argv[0]);
    argv++;
    argc--;
    show_CFG(1);

    u64 idx;
    for (int i = 0; i < argc; i++) {
        idx = strtoull(argv[i], NULL, 10);
        printf("%" PRIu64 "\n", idx);
        for (int j = 1; j < width; j++) {
            i2c(idx, _clear);
            printf(" --i2c--> %s ", _clear);
            hash(_clear, _hash);
            printf("--h--> ");
            for (int k = 0; k < CFG.hash_size; k++) {
                printf("%02x", _hash[k]);
            }
            idx = h2i(_hash, j, 0);
            printf(" --h2i(%d)--> %" PRIu64 "\n", j, idx);
        }
        printf("\n\n");
    }
    return 0;
}

int test_chain(int argc, char* argv[])
{
    if (argc < 2) {
        printf("wrong number of arguments\n");
        return 1;
    }
    show_CFG(1);

    int width;
    u64 idx;
    for (int i = 0; i < argc; i += 2) {
        width = strtol(argv[i], NULL, 10);
        idx = strtoull(argv[i + 1], NULL, 10);
        chain C = make_chain(width, 0, idx);
        printf("chain of length %d: %" PRIu64 " ... %" PRIu64 "\n", width, C.start, C.end);
    }
    return 0;
}

int test_search(int argc, char* argv[])
{
    if (argc != 2) {
        printf("wrong number of arguments\n");
        return 1;
    }

    char* filename = argv[0];
    u64 idx = strtoull(argv[1], NULL, 10);

    int height, width, n;
    chain* table = NULL;
    open_table(&height, &width, &n, &table, filename);

    int a, b;
    search_table_range(height, table, idx, &a, &b);
    if (search_table_range(height, table, idx, &a, &b) > 0) {
        printf("trouvé:\n  a = %d\n  b = %d\n", a, b);
        return 0;
    } else {
        printf("non trouvé\n");
        return 1;
    }
}

int main_test(int argc, char* argv[])
{
    if (argc < 1) {
        printf("wrong number of arguments\n");
        return 1;
    }
    char* test = argv[0];
    if (0 == strcmp("list", test)) {
        test_help();
        return 0;
    } else if (0 == strcmp("hash", test)) {
        return test_hash(argc - 1, argv + 1);
    } else if (0 == strcmp("config", test)) {
        return test_config(argc - 1, argv + 1);
    } else if (0 == strcmp("i2c", test)) {
        return test_i2c(argc - 1, argv + 1);
    } else if (0 == strcmp("c2i", test)) {
        return test_c2i(argc - 1, argv + 1);
    } else if (0 == strcmp("h2i", test)) {
        return test_h2i(argc - 1, argv + 1);
    } else if (0 == strcmp("i2i", test)) {
        return test_i2i(argc - 1, argv + 1);
    } else if (0 == strcmp("time_i2i", test)) {
        return test_time_i2i(argc - 1, argv + 1);
    } else if (0 == strcmp("full_chain", test)) {
        return test_full_chain(argc - 1, argv + 1);
    } else if (0 == strcmp("FULL_chain", test)) {
        return test_FULL_chain(argc - 1, argv + 1);
    } else if (0 == strcmp("chain", test)) {
        return test_chain(argc - 1, argv + 1);
    } else if (0 == strcmp("search", test)) {
        return test_search(argc - 1, argv + 1);
    } else {
        printf("Unknown test\n");
        test_help();
        return 1;
    }
}

// vim: textwidth=120
