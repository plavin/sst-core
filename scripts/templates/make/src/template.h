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

#ifndef _ELEMENT_ALLCAPS_H
#define _ELEMENT_ALLCAPS_H

#include <sst/core/component.h>

class ELEMENT_PASCAL_CASE : public SST::Component {

public:
/* SST ELI macros */
        /* Register component */
	SST_ELI_REGISTER_COMPONENT(
		ELEMENT_PASCAL_CASE,                // Class name
		"ELEMENT_CAMEL_CASE",               // Name of library
		"ELEMENT_PASCAL_CASE",              // Lookup name for component
		SST_ELI_ELEMENT_VERSION( 1, 0, 0 ), // Component version
		"A description of your element",    // FIXME: Add description
		COMPONENT_CATEGORY_PROCESSOR        // FIXME: Other options:
                                            //    COMPONENT_CATEGORY_MEMORY,
                                            //    COMPONENT_CATEGORY_NETWORK,
                                            //    COMPONENT_CATEGORY_UNCATEGORIZED
	)

        /*
         * Document parameters.
         *  Required parameter format: { "paramname", "description", NULL }
         *  Optional parameter format: { "paramname", "description", "default value"}
         */
	SST_ELI_DOCUMENT_PARAMS(
		{ "printFrequency", "How frequently to print a message from the component", "5" },
		{ "repeats", "Number of repetitions to make", "10" }
	)

        /* Document ports (optional if no ports declared)
         *  Format: { "portname", "description", { "eventtype0", "eventtype1" } }
         */
        SST_ELI_DOCUMENT_PORTS( )

        /* Document statistics (optional if no statistics declared)
         *  Format: { "statisticname", "description", "units", "enablelevel" }
         */
        SST_ELI_DOCUMENT_STATISTICS( )

        /* Document subcomponent slots (optional if no subcomponent slots declared)
         *  Format: { "slotname", "description", "subcomponentAPI" }
         */
        SST_ELI_DOCUMENT_SUBCOMPONENT_SLOTS( )

/* Class members */
        // Constructor
	ELEMENT_PASCAL_CASE( SST::ComponentId_t id, SST::Params& params );

        // Destructor
        ~ELEMENT_PASCAL_CASE();

        // SST lifecycle functions (optional if not used)
	virtual void init(unsigned int phase) override;
        virtual void setup() override;
        virtual void complete(unsigned int phase) override;
	virtual void finish() override;

        // Clock handler
	bool clockTick( SST::Cycle_t currentCycle );

private:
	SST::Output output;
	SST::Cycle_t printFreq;
	SST::Cycle_t maxRepeats;
	SST::Cycle_t repeats;

};


#endif
