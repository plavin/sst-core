// Copyright 2009-2025 NTESS. Under the terms
// of Contract DE-NA0003525 with NTESS, the U.S.
// Government retains certain rights in this software.
//
// Copyright (c) 2009-2025, NTESS
// All rights reserved.
//
// This file is part of the SST software package. For license
// information, see the LICENSE file in the top level directory of the
// distribution.

#include <sst/core/sst_config.h> // This include is REQUIRED for all implementation files

#include "{{ELEMENT_NAME}}.h"

{{COMPONENT_NAME}}::{{COMPONENT_NAME}}( SST::ComponentId_t id, SST::Params& params ) :
    SST::Component(id), repeats(0) {

    output.init("{{COMPONENT_NAME}}-" + getName() + "-> ", 1, 0, SST::Output::STDOUT);

    printFreq  = params.find<SST::Cycle_t>("printFrequency", 5);
    maxRepeats = params.find<SST::Cycle_t>("repeats", 10);

    if( ! (printFreq > 0) ) {
    	output.fatal(CALL_INFO, -1, "Error: printFrequency must be greater than zero.\n");
    }

    output.verbose(CALL_INFO, 1, 0, "Config: maxRepeats=%" PRIu64 ", printFreq=%" PRIu64 "\n",
        static_cast<uint64_t>(maxRepeats), static_cast<uint64_t>(printFreq));

    // Just register a plain clock for this simple example
    registerClock("100MHz", new SST::Clock::Handler2<{{COMPONENT_NAME}}, &{{COMPONENT_NAME}}::clockTick>(this));

    // Tell SST to wait until we authorize it to exit
    registerAsPrimaryComponent();
    primaryComponentDoNotEndSim();
}

{{COMPONENT_NAME}}::~{{COMPONENT_NAME}}() { }

void {{COMPONENT_NAME}}::init(unsigned int phase) {
    output.verbose(CALL_INFO, 1, 0, "Component is participating in phase %d of init.\n", phase);
}

void {{COMPONENT_NAME}}::setup() {
    output.verbose(CALL_INFO, 1, 0, "Component is being setup.\n");
}

void {{COMPONENT_NAME}}::complete(unsigned int phase) {
    output.verbose(CALL_INFO, 1, 0, "Component is participating in phase %d of complete.\n", phase);
}

void {{COMPONENT_NAME}}::finish() {
    output.verbose(CALL_INFO, 1, 0, "Component is being finished.\n");
}


bool {{COMPONENT_NAME}}::clockTick( SST::Cycle_t currentCycle ) {

    if( currentCycle % printFreq == 0 ) {
        output.verbose(CALL_INFO, 1, 0, "Hello World!\n");
    }

    repeats++;

    if( repeats == maxRepeats ) {
        primaryComponentOKToEndSim();
        return true;    // Stop calling this clock handler
    } else {
        return false;   // Keep calling this clock handler
    }
}
