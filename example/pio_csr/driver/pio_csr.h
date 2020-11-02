//////////////////////////////////////////////////////
//
// Driver for pio CSR module
// Generated by Simple CSR Generator
// Created: 11/1/2020 18:5
//
//////////////////////////////////////////////////////


// =============================================
// Register: pio_read, Address: 0x0
// =============================================
#define PIO__PIO_READ
#define PIO__PIO_READ_ADDR                                  0x0

// Field: DATA, Offset: 0, Size: 32
#define PIO__PIO_READ__DATA__OFT                            0
#define PIO__PIO_READ__DATA__MASK                           0xffffffff
#define PIO__PIO_READ__DATA__get(data) \
        ((data & PIO__PIO_READ__DATA__MASK) >> PIO__PIO_READ__DATA__OFT)
#define PIO__PIO_READ__DATA__set(DATA) \
        ((DATA << PIO__PIO_READ__DATA__OFT) & PIO__PIO_READ__DATA__MASK)

#define PIO__PIO_READ__set(DATA) (\
        PIO__PIO_READ__DATA__set(DATA))


// =============================================
// Register: pio_write, Address: 0x4
// =============================================
#define PIO__PIO_WRITE
#define PIO__PIO_WRITE_ADDR                                 0x4

// Field: DATA, Offset: 0, Size: 32
#define PIO__PIO_WRITE__DATA__OFT                           0
#define PIO__PIO_WRITE__DATA__MASK                          0xffffffff
#define PIO__PIO_WRITE__DATA__get(data) \
        ((data & PIO__PIO_WRITE__DATA__MASK) >> PIO__PIO_WRITE__DATA__OFT)
#define PIO__PIO_WRITE__DATA__set(DATA) \
        ((DATA << PIO__PIO_WRITE__DATA__OFT) & PIO__PIO_WRITE__DATA__MASK)

#define PIO__PIO_WRITE__set(DATA) (\
        PIO__PIO_WRITE__DATA__set(DATA))


// =============================================
// Register: pio_ctrl_status, Address: 0x8
// =============================================
#define PIO__PIO_CTRL_STATUS
#define PIO__PIO_CTRL_STATUS_ADDR                           0x8

// Field: LEVEL_CAPTURE_EN, Offset: 0, Size: 1
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__OFT         0
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__MASK        0x1
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__get(data) \
        ((data & PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__MASK) >> PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__OFT)
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__set(LEVEL_CAPTURE_EN) \
        ((LEVEL_CAPTURE_EN << PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__OFT) & PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__MASK)

// Field: LEVEL_CAPTURED, Offset: 16, Size: 1
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__OFT           16
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__MASK          0x10000
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__get(data) \
        ((data & PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__MASK) >> PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__OFT)
#define PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__set(LEVEL_CAPTURED) \
        ((LEVEL_CAPTURED << PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__OFT) & PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__MASK)

// Field: SAMPLE, Offset: 17, Size: 14
#define PIO__PIO_CTRL_STATUS__SAMPLE__OFT                   17
#define PIO__PIO_CTRL_STATUS__SAMPLE__MASK                  0x7ffe0000
#define PIO__PIO_CTRL_STATUS__SAMPLE__get(data) \
        ((data & PIO__PIO_CTRL_STATUS__SAMPLE__MASK) >> PIO__PIO_CTRL_STATUS__SAMPLE__OFT)
#define PIO__PIO_CTRL_STATUS__SAMPLE__set(SAMPLE) \
        ((SAMPLE << PIO__PIO_CTRL_STATUS__SAMPLE__OFT) & PIO__PIO_CTRL_STATUS__SAMPLE__MASK)

#define PIO__PIO_CTRL_STATUS__set(SAMPLE, LEVEL_CAPTURED, LEVEL_CAPTURE_EN) (\
        PIO__PIO_CTRL_STATUS__SAMPLE__set(SAMPLE) | \
        PIO__PIO_CTRL_STATUS__LEVEL_CAPTURED__set(LEVEL_CAPTURED) | \
        PIO__PIO_CTRL_STATUS__LEVEL_CAPTURE_EN__set(LEVEL_CAPTURE_EN))


