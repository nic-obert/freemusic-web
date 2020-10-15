#pragma once

#define TO_REMOVE_LENGTH 11

const char* to_remove[TO_REMOVE_LENGTH] = 
{
    "(audio)",
    "(official audio)",
    " lyrics",  // here the space is intentional
    "(lyrics)",
    "(official video)",
    "[official video]",
    "[official audio]",
    "[audio]",
    "[lyrics]",
    "(official music video)",
    "[official music video)"
};

